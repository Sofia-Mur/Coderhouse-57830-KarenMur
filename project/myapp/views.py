from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClientForm, OrderForm, ProductForm, SignupForm
from .models import Client, Order, Product
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout



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
    else:  # Maneja el caso de POST
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp:client_list")  # Asegúrate de usar el espacio de nombres aquí también
    return render(request, "myapp/client_create.html", {"form": form})

def product_create(request):
    if request.method == "GET":
        form = ProductForm()
    else:  # Maneja el caso de POST
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp:product_list")  # Asegúrate de usar el espacio de nombres aquí también
    return render(request, "myapp/product_create.html", {"form": form})

def order_create(request):
    if request.method == "GET":
        form = OrderForm()
    else:  # Maneja el caso de POST
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp:order_list")  # Asegúrate de usar el espacio de nombres aquí también
    return render(request, "myapp/order_create.html", {"form": form})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Guarda la contraseña de manera segura
            user.save()
            messages.success(request, "Account created successfully!")
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('myapp:index')  # Redirige a la página principal
    else:
        form = SignupForm()
    return render(request, 'myapp/signup.html', {'form': form})  # Asegúrate de renderizar el formulario

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('myapp/index.html')  # Redirige al índice o a la página anterior
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "myapp/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('myapp/index.html')

def user_profile(request):
    return render(request, 'myapp/user_profile.html')  # Asegúrate de crear esta plantilla

def about(request):
    return render(request, 'myapp/about.html')