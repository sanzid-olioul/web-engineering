from .views import AlbumView,LoveAlbumView,CommentView
from django.urls import path

urlpatterns = [
    path('album/',AlbumView.as_view(),name='albums'),
    path('album/favourite/',LoveAlbumView.as_view(),name='loved_albums'),
    path('album/<uuid:id>',AlbumView.as_view(),name='single_album'),
    path('album/favourite/<uuid:id>',LoveAlbumView.as_view(),name='love_album'),
    path('review',CommentView.as_view(),name='add_review'),
]