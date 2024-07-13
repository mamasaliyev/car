from django import forms
from .models import Logo, Car, Contract

class LogoForm(forms.ModelForm):
    class Meta:
        model = Logo
        fields = ['title', 'description', 'image']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'description', 'km', 'year', 'price', 'color', 'order', 'image', 'logo']

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['month', 'year']
