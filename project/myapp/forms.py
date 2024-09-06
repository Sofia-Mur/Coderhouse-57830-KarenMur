from django import forms

from .models import Client, Order, Product


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class OrderForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Client.objects.all(), empty_label="Select a client"
    )
    servicio = forms.ModelChoiceField(
        queryset=Product.objects.filter(disponible=True), empty_label="Select a product"
    )

    class Meta:
        model = Order
        fields = "__all__"
        widgets = {"date_delivery": forms.DateTimeInput(attrs={"type": "datetime-local"})}
        