# kittyapp/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Campos personalizados podem ser adicionados aqui, se necessário
    # Por exemplo, vamos adicionar um campo para o número de telefone:
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Se você deseja adicionar mais campos personalizados, basta adicionar mais linhas aqui.

    def __str__(self):
        return self.username

