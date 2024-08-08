from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist, Album
from .forms import ArtistForm, AlbumForm
from django.http import HttpResponse
from django.template import loader

def index(request):
    artist = Artist.objects.order_by('name') 
    album = Album.objects.all()
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render({'artist': artist, 'album':album}, request))



# Vistas de Artista

def artist_detail(request, id_artist):
    artist = get_object_or_404(Artist, pk=id_artist)
    template = loader.get_template('artistdetail.html')
    context = {
        'artist': artist
    }
    return HttpResponse(template.render(context, request))


def add_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistForm()
    return render(request, 'artistedit.html', {'form': form})

def edit_artist(request, id_artist):
    artist = get_object_or_404(Artist, pk=id_artist)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'artistedit.html', {'form': form})

def remove_artist(request, id_artist):
    artist = get_object_or_404(Artist, pk=id_artist)
    artist.delete()
    return redirect('album_manager:index')

# Vistas de Álbum

def album_detail(request, id_album):
    album = get_object_or_404(Album, pk=id_album)
    return render(request, 'albumdetail.html', {'album': album})

def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm()
    return render(request, 'albumedit.html', {'form': form})

def edit_album(request, id_album):
    album = get_object_or_404(Album, pk=id_album)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albumedit.html', {'form': form})

def remove_album(request, id_album):
    album = get_object_or_404(Album, pk=id_album)
    album.delete()
    return redirect('album_manager:index')
