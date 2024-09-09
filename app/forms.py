# app/forms.py
from django import forms
from .models import Product, Veg,Fruit,Juice

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'cover', 'description', 'price', 'sold']

class VegForm(forms.ModelForm):
    class Meta:
        model = Veg
        fields = ['name', 'cover', 'description', 'price','sold']

class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'cover', 'description', 'price', 'sold']

class JuiceForm(forms.ModelForm):
    class Meta:
        model =Juice
        fields = ['name', 'cover', 'description', 'price','sold']
# forms.py

from django import forms
from .models import customuser


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = customuser
        fields = ['full_name', 'email', 'phone']  # List fields you want to update

