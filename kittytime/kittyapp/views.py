# kittyapp/views.py

from django.shortcuts import render
from .models import Cat

def home(request):
    return render(request, 'home.html',)
