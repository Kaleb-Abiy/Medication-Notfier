from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def register_user(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data['username']
            messages.success(request, f'Sucessfuly registered {user_name}')
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print('hello')
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            print(user)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                print('failed')
                messages.error(request, 'login failed')
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')




