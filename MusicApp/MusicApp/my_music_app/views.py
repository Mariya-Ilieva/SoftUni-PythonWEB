from django.shortcuts import render, redirect
from MusicApp.my_music_app.forms import ProfileForm, AlbumForm, AlbumDeleteForm
from MusicApp.my_music_app.models import Profile, Album


def index(request):
    user_profile = Profile.objects.first()
    albums = Album.objects.all()
    form = ProfileForm()
    if not user_profile:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(index)
        return render(request, 'home-no-profile.html', {'form': form})
    context = {
        'user_profile': user_profile,
        'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'add-album.html', {'form': form})


def details_album(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'album-details.html', {'album': album})


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'edit-album.html', {'form': form})


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumDeleteForm(instance=album)
    if request.method == 'POST':
        album.delete()
        return redirect(index)
    return render(request, 'delete-album.html', {'form': form})


def details_profile(request):
    user_profile = Profile.objects.first()
    albums = Album.objects.all()
    albums_count = len(albums)
    context = {
        'user_profile': user_profile,
        'albums_count': albums_count,
    }
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    user_profile = Profile.objects.first()
    albums = Album.objects.all()
    if request.method == 'POST':
        albums.delete()
        user_profile.delete()
        return redirect(index)
    return render(request, 'profile-delete.html')
