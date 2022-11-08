from django.shortcuts import render, redirect
from GamesPlay.games_play_app.forms import ProfileForm, ProfileEditForm, ProfileDeleteForm, GameForm, GameDeleteForm
from GamesPlay.games_play_app.models import Profile, Game


def index(request):
    profile = Profile.objects.first()
    return render(request, 'home-page.html', {'profile': profile})


def dashboard_page(request):
    profile = Profile.objects.first()
    games = Game.objects.all()
    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'dashboard.html', context)


def game_create(request):
    profile = Profile.objects.first()
    form = GameForm()
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(dashboard_page)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'create-game.html', context)


def game_details(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.get(pk=pk)
    context = {
        'profile': profile,
        'game': game,
    }
    return render(request, 'details-game.html', context)


def game_edit(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.get(pk=pk)
    form = GameForm(instance=game)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect(dashboard_page)
    context = {
        'profile': profile,
        'form': form,
        'game': game,
    }
    return render(request, 'edit-game.html', context)


def game_delete(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.get(pk=pk)
    form = GameDeleteForm(instance=game)
    if request.method == 'POST':
        form = GameDeleteForm(request.POST, instance=game)
        form.save()
        return redirect(dashboard_page)
    context = {
        'profile': profile,
        'form': form,
        'game': game,
    }
    return render(request, 'delete-game.html', context)


def profile_create(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'create-profile.html', {'form': form})


def profile_details(request):
    profile = Profile.objects.first()
    games = Game.objects.all()
    if profile.first_name and profile.last_name:
        visible_name = f'{profile.first_name} {profile.last_name}'
    elif profile.first_name:
        visible_name = f'{profile.first_name}'
    elif profile.last_name:
        visible_name = f'{profile.last_name}'
    else:
        visible_name = ''

    if games:
        average_rating = sum(game.rating for game in games)/games.count()
    else:
        average_rating = 0

    context = {
        'profile': profile,
        'visible_name': visible_name,
        'games': games,
        'average_rating': average_rating,
    }
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(instance=profile)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(profile_details)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    games = Game.objects.all()
    form = ProfileDeleteForm(instance=profile)
    if request.method == 'POST':
        games.delete()
        profile.delete()
        return redirect(index)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'delete-profile.html', context)
