from uuid import uuid4
from django.db import models
from django.utils.text import slugify
from user.models import User
from song.models import Song

class Playlist(models.Model):
    id = models.SlugField(primary_key=True,editable=False)
    playlist_name = models.CharField(max_length=250)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.id:
            obj =Playlist.objects.get(self.id)
            obj.delete()

        self.id = slugify(self.playlist_name)
        super().save(*args, **kwargs)

class PlaylistSong(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE)
    song = models.ForeignKey(Song,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id =uuid4()
        return super().save(*args, **kwargs)