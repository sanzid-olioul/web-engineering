from django.contrib import admin
from .models import Playlist,PlaylistSong
# Register your models here.
@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['creator',]

@admin.register(PlaylistSong)
class PlaylistSongAdmin(admin.ModelAdmin):
    list_display = ['playlist','song']