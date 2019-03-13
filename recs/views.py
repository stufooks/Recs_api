from django.http import JsonResponse

from .models import Song
# Create your views here.

def song_list(request):
    songs = Song.objects.all()
    songs_list = list(songs)
    return JsonResponse(songs_list, safe=False)