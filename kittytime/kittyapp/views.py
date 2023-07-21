from django.shortcuts import render, HttpResponse,  redirect, get_object_or_404
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import SessaoEstudo

def cadastro(request):
    if request.method == "GET":
        return render(request,'cadastro.html')
    else: 
        username= request.POST.get('username')
        email= request.POST.get('email')
        senha= request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Já existe um usuário com esse username')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return render(request, 'login.html')
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        if user: 
            login_django(request, user)
            return redirect('home')
            
        else:
            return HttpResponse('Email ou senha inválidos')

@login_required(login_url="/login/")
def home(request):
    return render(request, 'home.html', {'user': request.user})

def sessao(request):
    return render(request, 'sessao.html')

def lista_sessoes(request):
    sessoes = SessaoEstudo.objects.all()
    return render(request, 'sessao.html', {'sessoes': sessoes})

def adicionar_sessao(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        tempo_contado = request.POST['tempo_contado']
        SessaoEstudo.objects.create(titulo=titulo, descricao=descricao, tempo_contado=tempo_contado)
        return redirect('lista_sessoes')
    return render(request, 'sessao.html')

def atualizar_sessao(request, sessao_id):
    sessao = get_object_or_404(SessaoEstudo, pk=sessao_id)
    if request.method == 'POST':
        sessao.titulo = request.POST['titulo']
        sessao.descricao = request.POST['descricao']
        sessao.tempo_contado = request.POST['tempo_contado']
        sessao.save()
        return redirect('lista_sessoes')
    return render(request, 'sessao.html', {'sessao': sessao})

def excluir_sessao(request, sessao_id):
    sessao = get_object_or_404(SessaoEstudo, pk=sessao_id)
    sessao.delete()
    return redirect('lista_sessoes')