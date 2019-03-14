from django.db import models

# Create your models here.
class Song(models.Model):
    track = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)