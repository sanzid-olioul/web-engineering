from django.urls import path
from .views import CreatePlaylistView,AddToPlaylistView,PlayListView,SinglePlayListView
app_name = 'playlist'
urlpatterns = [
    path('playlist/',PlayListView.as_view(),name='all_playlist'),
    path('playlist/create/',CreatePlaylistView.as_view(),name='create_playlist'),
    path('playlist/add/',AddToPlaylistView.as_view(),name='add_to_playlist'),
    path('playlist/<slug:id>/',SinglePlayListView.as_view(),name='single_play_list'),
]
