from django.contrib import admin

# Register your models here.
from .models import Song, Book

admin.site.register(Song)
admin.site.register(Book)