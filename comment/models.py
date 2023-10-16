from uuid import uuid4
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from user.models import User

class Comment(models.Model):
    id = models.UUIDField(primary_key=True)
    comment = models.CharField(max_length=1000)
    commenter = models.ForeignKey(User,on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")

    def save(self, *args, **kwargs):
        if not self.id:
            self.id =uuid4()
        return super().save(*args, **kwargs)
