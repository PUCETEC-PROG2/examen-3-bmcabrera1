from django.urls import path
from . import views

app_name = 'album_manager'

urlpatterns = [
    # URLs de Artista

    path("", views.index, name="index"),

    path('artist/new/', views.add_artist, name='add_artist'),
    path('artist/<int:id_artist>/', views.artist_detail, name='artist_detail'),
    path('edit_artist/<int:id_artist>/', views.edit_artist, name='edit_artist'),
    path('remove/<int:id_artist>/', views.remove_artist, name='remove_artist'),

    # URLs de Álbum
    path('album/new/', views.add_album, name='add_album'),
    path('album/<int:id_album>/', views.album_detail, name='album_detail'),
    path('edit_album/<int:id_album>/', views.edit_album, name='edit_album'),
    path('remove_album/<int:id_album>/', views.remove_album, name='remove_album'),
]
