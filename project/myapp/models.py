from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    disponible = models.BooleanField(default=True)  # Campo agregado

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.client.name} on {self.date.strftime('%Y-%m-%d')}"

    def get_products(self):
        # Retorna los productos en un formato legible
        return ', '.join([product.name for product in self.product.all()])

