from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_users'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_users'
    )

