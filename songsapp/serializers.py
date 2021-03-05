from rest_framework import serializers
from .models import Song,PodCast,AudioBook

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','song_name','song_duration','song_uploaded_time',)
        model = Song

class PodcastSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','podcast_name','podcast_duration','podcast_uploaded_time','host','participants',)
        model = PodCast
    
class AudiobookSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','title','author','narrator','audio_duration','audio_uploaded_time',)
        model = AudioBook