from uuid import uuid4
from django.db import models
from user.models import User
from singer.models import Singer

def file_directory_path(instance, filename):
    *_,ext = filename.split('.')
    f_name = instance.album_name+'.'+ext
    return f'{instance.album_creator}/{instance.singer}/{f_name}'

class Album(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    album_name = models.CharField(max_length=25)
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE)
    album_creator = models.OneToOneField(User,on_delete=models.CASCADE)
    album_image = models.ImageField(upload_to=file_directory_path)
    album_bio = models.CharField(max_length=500)
    album_info = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created','album_name']
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id =uuid4()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.album_name


class AlbumLikedBy(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_subscribed = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_subscribed']
        verbose_name_plural = 'AlbumsLikedBy'
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id =uuid4()
        return super().save(*args, **kwargs)



