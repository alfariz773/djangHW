from django.shortcuts import render
from.forms import con_details
from.models import details
def contact(request):
    if request.method == 'POST':
        form = con_details(request.POST)
        if form.is_valid():
            cust = details()
            cust.name = form.cleaned_data['name']
            cust.email=form.cleaned_data['email']
            cust.phone=form.cleaned_data['phone']

            cust.save()
            return render(request,'result.html',{
                'name':cust.name     
            })
    else:
        form= con_details()
    return render(request,'contact.html',{'form':form})
            