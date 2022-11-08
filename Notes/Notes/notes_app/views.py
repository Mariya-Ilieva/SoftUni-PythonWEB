from django.shortcuts import render, redirect
from Notes.notes_app.models import Profile, Note
from Notes.notes_app.forms import CreateNote, EditNote, DeleteNote, CreateProfile


def index(request):
    profile_user = Profile.objects.first()
    notes = Note.objects.all()
    form = CreateProfile()
    if not profile_user:
        if request.method == 'POST':
            form = CreateProfile(request.POST, instance=profile_user)
            if form.is_valid():
                form.save()
                return redirect(index)
        return render(request, 'home-no-profile.html', {'form': form})
    return render(request, 'home-with-profile.html', {'notes': notes})


def user_profile(request):
    profile_user = Profile.objects.first()
    count_of_notes = Note.objects.all().count()
    context = {
        'profile_user': profile_user,
        'count_of_notes': count_of_notes
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile_user = Profile.objects.first()
    notes = Note.objects.all()
    profile_user.delete()
    notes.delete()
    return redirect(index)


def create_note(request):
    profile_user = Profile.objects.first()
    form = CreateNote()
    context = {
        'form': form,
        'profile_user': profile_user,
    }
    if request.method == 'POST':
        form = CreateNote(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    form = EditNote(instance=note)
    profile_user = Profile.objects.first()
    context = {
        'form': form,
        'profile_user': profile_user,
    }
    if request.method == 'POST':
        form = EditNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(index)

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    form = DeleteNote(instance=note)
    profile_user = Profile.objects.first()
    context = {
        'form': form,
        'profile_user': profile_user,
    }
    if request.method == 'POST':
        form = DeleteNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(index)

    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    profile_user = Profile.objects.first()
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
        'profile_user': profile_user,
    }
    return render(request, 'note-details.html', context)
