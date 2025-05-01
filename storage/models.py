from django.db import models


class StorageItem(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()