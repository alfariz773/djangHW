from django.shortcuts import render,redirect
from .models import Std
from .forms import std_from


def home(request):
    student = Std.objects.all()
    return render(request, 'recordapp/home.html', {'student': student})

    
def add(request):
    if request.method == 'POST':
        form = std_from(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = std_from()
    return render(request, 'recordapp/add.html', {'form': form})    

def edit(request,pk):
    student = Std.objects.get(pk=pk)
    if request.method == 'POST':
        form = std_from(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form= std_from(instance=student)
    return render(request, 'recordapp/edit.html', {'form': form})  

def delete(request, pk):
    student = Std.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'recordapp/delete.html', {'student': student})  


            

