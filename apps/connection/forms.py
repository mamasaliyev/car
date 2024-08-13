from django import forms
from django.forms import Textarea, TextInput, EmailInput

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'subject': Textarea(attrs={'class': 'form-control'}),
        }
