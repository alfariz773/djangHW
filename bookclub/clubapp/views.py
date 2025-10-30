from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
             # Auto login after signup
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'clubapp/signup.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('welcome')
    else:
        form = AuthenticationForm()
    return render(request, 'clubapp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def welcome(request):
    visits = request.session.get('visits', 0)
    visits += 1
    request.session['visits'] = visits
    return render(request, 'clubapp/welcome.html', {'visits': visits})
