from django import forms
from .models import Artist, Album

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'country']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'year', 'gender', 'artist', 'front_page']
