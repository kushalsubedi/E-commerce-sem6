from django.contrib import admin

# Register your models here.
from .models import Product,category

admin.site.register(category)
admin.site.register(Product)