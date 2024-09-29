from django import forms
from django.contrib.auth.models import User
from .models import Client, Order, Product, UserProfile
from django.core.exceptions import ValidationError

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
        widgets = {
            "date_delivery": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        
