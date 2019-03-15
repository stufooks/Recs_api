from django.urls import path
from . import views

urlpatterns = [
    path('songs', views.song_list),
    path('songs/new', views.song_create),
    path('songs/delete', views.song_delete),
    path('books', views.book_list),
    path('books/new', views.book_create),
    path('books/delete', views.book_delete),
]