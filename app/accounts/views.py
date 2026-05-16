from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm, UserLoginForm

def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cinema:cinema_list') 
    else:
        form = UserRegistrationForm()
        
    return render(request, 'accounts/register.html', context={'form': form})

def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) 
            return redirect('cinema:cinema_list')
    else:
        form = UserLoginForm()
        
    return render(request, 'accounts/login.html', context={'form': form})

def user_logout_view(request):
    if request.method == 'POST':
        logout(request) 
        return redirect('cinema:cinema_list')
        
    return render(request, 'accounts/logout_confirm.html')
