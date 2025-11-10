from django import forms
from .models import weightsubmit

class weightsubmitform(forms.ModelForm):
    class Meta:
        model = weightsubmit
        fields = ['weight']   
