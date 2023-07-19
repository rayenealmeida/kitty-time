from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from .forms import CadastroForm

def home(request):
    if not request.user.is_authenticated:
        return redirect('cadastro')
    
    return render(request, 'home.html')

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CadastroForm()
    
    return render(request, 'cadastro.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})
