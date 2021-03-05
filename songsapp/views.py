from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import SongSerializer,PodcastSerializer,AudiobookSerializer

from .models import Song,PodCast,AudioBook

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class PodCastList(generics.ListCreateAPIView):
    queryset = PodCast.objects.all()
    serializer_class = PodcastSerializer

class PodCastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PodCast.objects.all()
    serializer_class = PodcastSerializer

class AudioBookList(generics.ListCreateAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudiobookSerializer

class AudioBookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudiobookSerializer