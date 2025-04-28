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
    

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assigned = models.ManyToManyField(User, related_name='tasks', blank=True)  # Zuordnung zu Usern
    due_date = models.DateField()
    priority = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    bucket = models.CharField(max_length=50, default='todo')

    def __str__(self):
        return self.title

class SubTask(models.Model):
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=255)
    subdone = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subtitle} ({'Done' if self.subdone else 'Open'})"