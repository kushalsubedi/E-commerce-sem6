from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=50000)
    image = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.name
    def summary(self):
        return self.body[:300]
     
    def pub_date_pretty(self):
        return self.created_at.strftime('%b %e %Y')
    
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class Order (models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=True)
    transaction_id=models.CharField(max_length=120,null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
class shippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    zipcode=models.CharField(max_length=200,null=True)
    date_added =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
