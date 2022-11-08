from django.shortcuts import render, redirect
from online_library.online_library_app.forms import ProfileForm, BookForm, BookEditForm, ProfileEditForm, ProfileDeleteForm
from online_library.online_library_app.models import Profile, Book


def index(request):
    user_profile = Profile.objects.first()
    books = Book.objects.all()
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
        'books': books,
    }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    user_profile = Profile.objects.first()
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    context = {
        'form': form,
        'user_profile': user_profile,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    user_profile = Profile.objects.first()
    book = Book.objects.get(pk=pk)
    form = BookEditForm(instance=book)
    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(index)
    context = {
        'user_profile': user_profile,
        'book': book,
        'form': form,
    }
    return render(request, 'edit-book.html', context)


def details_book(request, pk):
    user_profile = Profile.objects.first()
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
        'user_profile': user_profile,
    }
    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect(index)


def profile(request):
    user_profile = Profile.objects.first()
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    user_profile = Profile.objects.first()
    form = ProfileEditForm(instance=user_profile)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect(index)
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    user_profile = Profile.objects.first()
    books = Book.objects.all()
    form = ProfileDeleteForm(instance=user_profile)
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=user_profile)
        if form.is_valid():
            books.delete()
            form.save()
            return redirect(index)
        return render(request, 'delete-profile.html', {'form': form})
    context = {
        'form': form,
        'user_profile': user_profile,
    }
    return render(request, 'delete-profile.html', context)
