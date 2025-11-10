from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone
from .models import weightsubmit
from .forms import weightsubmitform
from django.db.models import Min, Max



def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'sign.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('addweight')
    else:
        form = AuthenticationForm()
    return render(request, 'log_in.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def addweight(request):
    today = timezone.now().date()
    if weightsubmit.objects.filter(user=request.user, date=today).exists():
        return render(request, 'add.html', {
            'error': 'You have already added weight today!'
        })

    if request.method == 'POST':
        form = weightsubmitform(request.POST)
        if form.is_valid():
            weight_entry = form.save(commit=False)
            weight_entry.user = request.user
            weight_entry.save()
            return redirect('weight_list')
    else:
        form = weightsubmit()
    return render(request, 'add.html', {'form': form})


@login_required
def weight_list(request):
    weights = weightsubmit.objects.filter(user=request.user).order_by('-date', '-time')
    paginator = Paginator(weights, 1)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'weight_list.html', {'page_obj': page_obj})

@login_required
def weight_loss(request):
    result = None
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        
        data = weightsubmit.objects.filter(
            user=request.user,
            date__range=[start_date, end_date]
        ).aggregate(start_weight=Min('weight'), end_weight=Max('weight'))

        if data['start_weight'] is not None and data['end_weight'] is not None:
            result = data['start_weight'] - data['end_weight']
        else:
            result = "No weight entries found in this range."

    return render(request, 'loss.html', {'result': result})



@login_required
def edit(request, pk):
    entry = weightsubmit.objects.get(pk=pk)
    if request.method == 'POST':
        form = weightsubmitform(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('addweight')
    else:
        form = weightsubmitform(instance=entry)
    return render(request, 'edit.html', {'form': form})

@login_required
def delete(request, pk):
    entry = weightsubmit.objects.get(pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('addweight')
    return render(request, 'delete.html', {'entry': entry})


