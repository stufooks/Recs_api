from django.http import JsonResponse
import json

from .models import Song
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