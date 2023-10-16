from collections.abc import Iterable
import mutagen
from uuid import uuid4
from django.db import models
from user.models import User
from album.models import Album

def file_directory_path(instance, filename):
    *_,ext = filename.split('.')
    f_name = instance.song_title +'.'+ext
    return f'{instance.song_album.album_creator}/{instance.song_album}/{f_name}'

class Song(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    song_title = models.CharField(max_length=250)
    song_album = models.ForeignKey(Album,on_delete=models.CASCADE)
    song = models.FileField(upload_to=file_directory_path)
    song_duration = models.CharField(max_length = 50,null=True,blank = True,editable = False)
    song_extension = models.CharField(max_length = 10,blank=True,null=True,editable = False)
    date_created = models.DateField(auto_now_add=True)

    def save(self,*arg,**kwarg):
        self.id = uuid4()
        ln = mutagen.File(self.song).info.length
        ln = str(int(ln//3600)) +':'+ str(int((ln - 3600*(ln//3600))//60)) + ':'+str(int(round(ln - (3600*(ln//3600)+ 60*(ln//60)))))
        self.song_duration = ln
        file_name = self.song.name
        *_,ext = file_name.split('.')
        self.song_extension = ext
        return super().save(*arg,**kwarg)
    
    
    
    def __str__(self):
        return self.song_title

class SongLikedBy(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    song = models.ForeignKey(Song,on_delete=models.Case)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_likes = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_likes']
        verbose_name_plural = 'SongsLikedBy'
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id =uuid4()
        return super().save(*args, **kwargs)

class RecentlyPlayed(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    song = models.ForeignKey(Song,on_delete=models.Case)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_played = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_played']
        verbose_name_plural = 'RecentlyPlayed'

    def save(self, *args, **kwargs):
        if not self.id:
            self.id =uuid4()
        return super().save(*args, **kwargs)
