from django.contrib import admin
from .models import Client, Order, Product, UserProfile

admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(UserProfile)



