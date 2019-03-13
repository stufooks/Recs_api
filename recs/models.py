from django.db import models

# Create your models here.
class Song(models.Model):
    track = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)