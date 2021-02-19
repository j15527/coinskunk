from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from main_app.models import Portfolio


def home(request):
    return render(request, 'auth/home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('main')
        else:
            messages.success(request, 'Error, Check your credentials and try again or register for an account.')

            return redirect('login')

    else:
        return render(request, 'auth/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            create_portfolio(user)
            messages.success(request, 'Congratulations, you have successfully registered')
            return redirect('main')
    else:
        form = UserCreationForm()
    context = {'form': form, }
    return render(request, 'auth/register.html', context)


def create_portfolio(user):
    p = Portfolio(user=user)
    p.save(force_insert=True)
