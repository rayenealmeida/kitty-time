from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cat
class CatForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Cat
        fields = ['username', 'email', 'password1', 'password2']
