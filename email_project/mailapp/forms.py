from django import forms
from .models import Product

class PrdtForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
