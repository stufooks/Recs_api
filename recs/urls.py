from django.urls import path
from . import views

urlpatterns = [
    path('songs', views.song_list),
    path('songs/new', views.song_create),
    path('songs/delete', views.song_delete),
    path('books', views.song_list),
    path('books/new', views.song_create),
    path('books/delete', views.song_delete),
]