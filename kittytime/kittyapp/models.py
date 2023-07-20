from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Cat(AbstractUser):
    email = models.EmailField(unique=True)

    # Adicionar o related_name aos campos groups e user_permissions
    groups = models.ManyToManyField(Group, related_name='cats')
    user_permissions = models.ManyToManyField(Permission, related_name='cats')

    def __str__(self):
        return self.username
