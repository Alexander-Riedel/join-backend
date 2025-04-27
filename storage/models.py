from django.db import models


# Create your models here.
class StorageItem(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.JSONField()  # oder TextField(), je nachdem
    created_at = models.DateTimeField(auto_now_add=True)
