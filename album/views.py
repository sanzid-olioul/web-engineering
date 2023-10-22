from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Count
from .models import Album,AlbumLikedBy
from song.models import Song
from user.models import UserProfile
from comment.models import Review
# Create your views here.
class AlbumView(View):
    def get(self,request,*args, **kwargs):
        try:
            album_id = kwargs['id']
            album = Album.objects.get(pk=album_id)
            songs = Song.objects.filter(song_album=album)
            return render(request,'album/album.html',{'album':album,'songs':songs})
        except:
            albums = Album.objects.annotate(number_of_songs=Count('song')).annotate(number_of_loves=Count('albumlikedby'))
            return render(request,'album/album_list.html',{'albums':albums})

class LoveAlbumView(View):
    def get(self,request,*args, **kwargs):
        try:
            album_id = kwargs['id']
            album = Album.objects.get(pk=album_id)
            liked_album = AlbumLikedBy.objects.filter(user=request.user,album=album)
            if len(liked_album):
                liked_album[0].delete()
            else:
                AlbumLikedBy.objects.create(user = request.user,album=album)
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        except:
            albums = Album.objects.filter(albumlikedby__user=request.user).annotate(number_of_songs=Count('song')).annotate(number_of_loves=Count('albumlikedby'))
            return render(request,'album/album_list.html',{'albums':albums})
        
class CommentView(View):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        
        review = request.POST['review']
        rating = request.POST['star']
        album_id = request.POST['album_id']
        album = Album.objects.get(id=album_id)

        Review.objects.create(review=review,reviewer=request.user,rating=rating,content_object=album)
        
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    
