from django.http import JsonResponse
import json

from .models import Song, Book
# Create your views here.

def song_list(request):
    songs = Song.objects.all().values()
    songs_list = list(songs)
    return JsonResponse(songs_list, safe=False)

def song_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Song.objects.create(track=data['track'], artist=data['artist'])
        return JsonResponse("create successful", safe=False)

def song_delete(request):
    if request.method == "DELETE":
        data = json.loads(request.body)
        Song.objects.filter(id=data['rowData']['id']).delete()
        return JsonResponse("delete successful", safe=False)

def book_list(request):
    books = Book.objects.all().values()
    books_list = list(books)
    return JsonResponse(books_list, safe=False)

def song_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Book.objects.create(track=data['title'], artist=data['author'])
        return JsonResponse("create successful", safe=False)

def song_delete(request):
    if request.method == "DELETE":
        data = json.loads(request.body)
        Book.objects.filter(id=data['rowData']['id']).delete()
        return JsonResponse("delete successful", safe=False)
