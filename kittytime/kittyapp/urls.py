from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),    
    path('list-sessions/', views.list_sessions, name='list_sessions'),
    path('create-session/', views.create_session, name='create_session'),
    path('update-session/<int:session_id>/', views.update_session, name='update_session'),
    path('delete-session/<int:session_id>/', views.delete_session, name='delete_session'),
]
