from django.shortcuts import redirect, render

from .forms import ClientForm, OrderForm, ProductForm
from .models import Client, Order, Product


def index(request):
    return render(request, "myapp/index.html")


def client_list(request):
    query = Client.objects.all()
    context = {"object_list": query}
    return render(request, "myapp/client_list.html", context)


def product_list(request):
    query = Product.objects.all()
    context = {"object_list": query}
    return render(request, "myapp/product_list.html", context)


def order_list(request):
    query = Order.objects.all()
    context = {"object_list": query}
    return render(request, "myapp/order_list.html", context)


def client_create(request):
    if request.method == "GET":
        form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("client_list")
    return render(request, "myapp/client_create.html", {"form": form})


def product_create(request):
    if request.method == "GET":
        form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    return render(request, "myapp/product_create.html", {"form": form})


def order_create(request):
    if request.method == "GET":
        form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_list")
    return render(request, "myapp/order_create.html", {"form": form})
