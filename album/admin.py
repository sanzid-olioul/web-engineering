from django.contrib import admin
from .models import Album,AlbumLikedBy
from user.models import User
from song.models import Song


class SongInline(admin.StackedInline):
    model = Song
    extra = 1

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_name','singer','album_bio','album_creator']
    list_filter = ['singer',]
    search_fields = ['album_name','singer','album_creator']
    exclude = ['album_creator']
    inlines = [SongInline,]

    def save_model(self, request, obj, form, change):
        obj.album_creator = request.user
        super().save_model(request, obj, form, change)


@admin.register(AlbumLikedBy)
class AlbumLikedByAdmin(admin.ModelAdmin):
    list_display = ['album','user']
    list_filter =  ['album','user']
    search_fields = ['album','user']

    def has_add_permission(self, request):
        return False