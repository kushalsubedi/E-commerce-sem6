from django.db import models
from django.contrib.auth.models import User
from Home.models import Product
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    def get_total(self):
        total = 0
        for product in self.products.all():
            total += product.price
        return total 


