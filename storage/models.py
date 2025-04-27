from django.db import models


# Create your models here.
class StorageItem(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.JSONField()  # oder TextField(), je nachdem
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # wichtig: jede E-Mail soll nur einmal vorkommen
    password = models.CharField(max_length=255)
    color = models.CharField(max_length=7)  # Hex-Farbe wie "#aabbcc"
    initials = models.CharField(max_length=5)

    def __str__(self):
        return self.name