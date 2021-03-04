from django.contrib import admin
from .models import Song,PodCast,AudioBook

# Register your models here.
admin.site.register(Song)
admin.site.register(PodCast)
admin.site.register(AudioBook)