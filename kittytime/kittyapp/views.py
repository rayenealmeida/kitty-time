from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirecionar para a página inicial após o login
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedido
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        # Processar o formulário e criar um novo usuário
        pass
    else:
        return render(request, 'user_create.html')

def user_update(request, id):
    user = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        # Processar o formulário e atualizar o usuário
        pass
    else:
        return render(request, 'user_update.html', {'user': user})

def user_delete(request, id):
    user = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        # Excluir o usuário
        pass
    else:
        return render(request, 'user_delete.html', {'user': user})

