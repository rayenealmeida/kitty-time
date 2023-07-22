from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),    
   #CRUD
    path('sessao/', views.sessao, name='sessao'),  
    path('sessao/lista/', views.lista_sessoes, name='lista_sessoes'),  
    path('sessao/adicionar/', views.adicionar_sessao, name='adicionar_sessao'),
    path('sessao/atualizar/<int:sessao_id>/', views.atualizar_sessao, name='atualizar_sessao'),
    path('sessao/excluir/<int:sessao_id>/', views.excluir_sessao, name='excluir_sessao'),
]
