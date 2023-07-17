from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser

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

