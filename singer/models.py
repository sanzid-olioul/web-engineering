from uuid import uuid4
from django.db import models

class Singer(models.Model):
    id = models.SlugField(primary_key=True,editable=False)
    singer_name = models.CharField(max_length=50,)
    singer_avater = models.ImageField(blank=True,null=True)
    singer_bio = models.TextField()
    date_of_birth = models.DateField(blank=True,null=True)
    birth_place = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id =uuid4()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.singer_name