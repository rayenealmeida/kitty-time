from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from .forms import CadastroForm, CatForm  # Importe o formulário CatForm
from .models import Cat 

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

def cat_list(request):
    cats = Cat.objects.all()
    return render(request, 'cat_list.html', {'cats': cats})

def cat_detail(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    return render(request, 'cat_detail.html', {'cat': cat})

def cat_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CatForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('cat_list')
        else:
            form = CatForm()
        return render(request, 'cat_create.html', {'form': form})
    else:
        return redirect('login')
    
def cat_update(request, cat_id):
    if request.user.is_authenticated:
        cat = get_object_or_404(Cat, id=cat_id)
        if request.method == 'POST':
            form = CatForm(request.POST, instance=cat)
            if form.is_valid():
                form.save()
                return redirect('cat_detail', cat_id=cat_id)
        else:
            form = CatForm(instance=cat)
        return render(request, 'cat_update.html', {'form': form, 'cat': cat})
    else:
        return redirect('login')
    
def cat_delete(request, cat_id):
    if request.user.is_authenticated:
        cat = get_object_or_404(Cat, id=cat_id)
        if request.method == 'POST':
            cat.delete()
            return redirect('cat_list')
        return render(request, 'cat_delete.html', {'cat': cat})
    else:
        return redirect('login')