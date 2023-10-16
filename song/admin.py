from django.contrib import admin
from .models import Song,SongLikedBy,RecentlyPlayed

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_title','song_album','song']
    list_filter = ['song_album']
    search_fields = ['song_title']
    readonly_fields = ['song_title','song_album','song','date_created']

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

@admin.register(SongLikedBy)
class SongLikedByAdmin(admin.ModelAdmin):
    list_display = ['song','user']
    list_filter = ['song','user']
    search_fields = ['song','user']

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

@admin.register(RecentlyPlayed)
class RecentlyPlayedAdmin(admin.ModelAdmin):
    list_display = ['song','user']
    list_filter = ['song','user']
    search_fields = ['song','user']

    # def has_add_permission(self, request):
    #     return True
    
    # def has_change_permission(self, request, obj=None):
    #     return False
    
    # def has_delete_permission(self, request, obj=None):
    #     return False

    # def save_model(self, request, obj, form, change):
    #     return True

    # def delete_model(self, request, obj):
    #     pass