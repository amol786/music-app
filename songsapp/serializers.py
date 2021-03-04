from rest_framework import serializers
from .models import Song,PodCast,AudioBook

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        field = ('id','song_name','song_duration','song_updated_time',)
        model = Song

