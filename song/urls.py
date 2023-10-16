from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import RecentlyPlayedView,FavouriteSongView

urlpatterns = [
    path('recent/',login_required(RecentlyPlayedView.as_view()),name='recent_songs'),
    path('favourite/',login_required(FavouriteSongView.as_view()),name='favourite_songs'),
    path('favourite/<uuid:id>',login_required(FavouriteSongView.as_view()),name='add_favourite'),
    path('song/play/<uuid:id>',login_required(FavouriteSongView.as_view()),name='play_song'),
    
]
