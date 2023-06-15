from django import forms
from .models import Product,category
input_css_class = 'form-control'
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','name','body','price','image']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class
