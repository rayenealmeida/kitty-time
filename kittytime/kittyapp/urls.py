from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('cats/', views.cat_list, name='cat_list'),  
    path('cats/<int:cat_id>/', views.cat_detail, name='cat_detail'), 
    path('cats/create/', views.cat_create, name='cat_create'),  
    path('cats/<int:cat_id>/update/', views.cat_update, name='cat_update'),  
    path('cats/<int:cat_id>/delete/', views.cat_delete, name='cat_delete'),  
]
