from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Order, Customer, Checkout

class UserRgisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']
class CreateorderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        exclude=['status']
 
class CreateproductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
 
class CreatecustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = '__all__'
