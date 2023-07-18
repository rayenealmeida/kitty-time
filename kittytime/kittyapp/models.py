# kittyapp/models.py

from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)

    def __str__(self):
        return self.name
