from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
input_css_class = 'form-control'
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class
    
    #validate passwords
    # def clean(self):
    #     cleaned_data = super(CreateUserForm, self).clean()
    #     password = cleaned_data.get('password1')
    #     confirm_password = cleaned_data.get('password2')
    #     if password != confirm_password:
    #         raise forms.ValidationError(
    #             "password and confirm_password does not match"
    #         )
    #         print("password and confirm_password does not match")
    #     else:
    #         return cleaned_data
    #         print("password and confirm_password match")
        