from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import SongSerializer

from .models import Song

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer