from django.db import models
from embed_video.fields import EmbedVideoField

class Video(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField(default="https://youtu.be/dQw4w9WgXcQ") 

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['added']