from django import forms
from .models import Product,category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','name','body','image']