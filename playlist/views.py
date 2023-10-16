from django.shortcuts import render,redirect
from django.views import View
from .models import Playlist,PlaylistSong
from song.models import Song
from django.db.models.aggregates import Count
# Create your views here.
class CreatePlaylistView(View):
    def get(self,request,*args, **kwargs):
        ls = Playlist.objects.all()[0]
        songs = PlaylistSong.objects.filter(playlist=ls)
        return render(request,'playlist/create_playlist.html',{'songs':songs})
    def post(self, request, *args, **kwargs):
        Playlist.objects.create(playlist_name =request.POST['playlist_name'],creator=request.user)
        return render(request,'playlist/create_playlist.html')
    
class AddToPlaylistView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'playlist/add_to_playlist.html')
    
    def post(self, request, *args, **kwargs):
        playlist_id = request.POST['playlist']
        song_id = request.POST['song_id']

        pl=Playlist.objects.get(id=playlist_id)
        sg=Song.objects.get(id=song_id)

        PlaylistSong.objects.create(playlist=pl,song=sg)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    
class PlayListView(View):
    def get(self,request,*args, **kwargs):
        
        playlists = Playlist.objects.filter(creator = request.user)
        print(playlists)
        return render(request,'playlist/playlists.html',{'playlists':playlists})
    
class SinglePlayListView(View):
    def get(self,request,*args, **kwargs):
        songs = PlaylistSong.objects.filter(playlist__id=kwargs['id'])
        number_of_songs = len(songs)
        playlist = Playlist.objects.get(id=kwargs['id'])
        
        return render(request,'playlist/create_playlist.html',{'songs':songs,'number_of_songs':number_of_songs,'playlist':playlist})
