from django import forms
from .models import customer

class coustdetails(forms.ModelForm):
    class Meta:
        model=customer
        fields=['name','email']
       