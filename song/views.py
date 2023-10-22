from django.shortcuts import render,redirect
from django.views import View
from .models import Song,RecentlyPlayed,SongLikedBy
from playlist.models import Playlist

class RecentlyPlayedView(View):
    def get(self,request,*args, **kwargs):
        recent = Song.objects.filter(recentlyplayed__user=request.user)
        return render(request,'song/song_list.html',{'songs':recent})

class FavouriteSongView(View):
    def get(self,request,*args, **kwargs):
        try:
            song_id = kwargs['id']
            song = Song.objects.get(pk=song_id)
            remove_fav = SongLikedBy.objects.filter(song=song,user=request.user)
            if len(remove_fav):
                remove_fav[0].delete()
            else:
                SongLikedBy.objects.create(user=request.user,song=song)
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        except:
            favourite_songs = Song.objects.filter(songlikedby__user=request.user)
            playlists = Playlist.objects.filter(creator=request.user)
            return render(request,'song/song_list.html',{'songs':favourite_songs,'playlists':playlists})