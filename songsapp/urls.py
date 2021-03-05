from django.urls import path
from .views import SongList, SongDetail, PodCastList,PodCastDetail,AudioBookList,AudioBookDetail

urlpatterns=[
    path('song/<int:pk>/',SongDetail.as_view()),
    path('song/',SongList.as_view()),
    path('podcast/<int:pk>/',PodCastDetail.as_view()),
    path('podcast/',PodCastList.as_view()),
    path('audiobook/<int:pk>/',AudioBookDetail.as_view()),
    path('audiobook/',AudioBookList.as_view()),
]