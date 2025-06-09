from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from .decorators import role_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('home'))
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

@role_required('director')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})
    