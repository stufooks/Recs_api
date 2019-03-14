from django.urls import path
from . import views

urlpatterns = [
    path('songs', views.song_list),
    path('songs/new', views.song_create)
]