from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class SessaoEstudo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tempo_contado = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo
