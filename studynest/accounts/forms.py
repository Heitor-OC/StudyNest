from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'nota_conhec_basicos', 'nota_conhec_especificos', 'nota_final', 'concorrencia']      


"""class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' # ['customer', 'product', ...]"""
        

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        