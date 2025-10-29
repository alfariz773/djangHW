from django import forms
from.models import Std

class std_from(forms.ModelForm):
    class Meta:
        model= Std
        fields=['Name','standard','age']
    
   
    
