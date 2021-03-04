from django.db import models
#from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Song(models.Model):
    song_name = models.CharField(max_length=100)
    song_duration = models.PositiveIntegerField()
    song_uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.song_name

class PodCast(models.Model):
    podcast_name = models.CharField(max_length=100)
    podcast_duration = models.PositiveIntegerField()
    podcast_uploaded_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)
    participants = models.TextField(null=True,blank=True)
    #participants = ArrayField(
    #        models.CharField(max_length=100, blank=True),
    #        size=10,
    #        default=list,
    #    )

    def __str__(self):
        return self.podcast_name
    

class AudioBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    audio_duration = models.PositiveIntegerField()
    audio_uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title