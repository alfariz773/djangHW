from django.shortcuts import render, redirect
from .models import customer
from .forms import coustdetails

def list_coustomer(request):
    if request.method == 'POST':
        form = coustdetails(request.POST)
        if form.is_valid():
            form.save()
            return  redirect("all_coustomers")
    else:
        form= coustdetails()
        return render(request, 'submit.html',{'form':form})
def all_coustom(request):
    customers = customer.objects.all().order_by('name')
    return render(request, 'all_coustomer.html', {'customers': customers})
def filter(request):
    customers = customer.objects.filter(email__endswith='@example.com').order_by('name')
    return render(request, 'filter.html', {'customers': customers})
      
    

# Create your views here.
