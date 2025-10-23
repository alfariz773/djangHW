from django import forms

class con_details(forms.Form):
    name= forms.CharField(max_length=100)
    email= forms.EmailField()
    phone= forms.CharField(max_length=12)
    
