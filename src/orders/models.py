from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse 
from Home.models import Product 


# Create your models here.
class Order (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order: {self.user.username} - {self.created.strftime('%d/%m/%Y')}"
    def get_total(self):
        total = 0
        for product in self.products.all():
            total += product.price
        return total
    def update_products(self):
        for product in self.products.all():
            product.stock -= 1
            product.save()

