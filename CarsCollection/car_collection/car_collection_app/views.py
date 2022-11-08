from django.shortcuts import render, redirect
from car_collection.car_collection_app.forms import ProfileForm, CarForm, CarDeleteForm, ProfileEditForm, ProfileDeleteForm
from car_collection.car_collection_app.models import Profile, Car


def index(request):
    user_profile = Profile.objects.first()
    context = {
        'user_profile': user_profile
    }
    return render(request, 'index.html', context)


def catalogue_page(request):
    user_profile = Profile.objects.first()
    cars = Car.objects.all()
    context = {
        'user_profile': user_profile,
        'cars': cars,
    }
    return render(request, 'catalogue.html', context)


def car_create(request):
    user_profile = Profile.objects.first()
    form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(catalogue_page)
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'car-create.html', context)


def car_details(request, pk):
    user_profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)
    context = {
        'user_profile': user_profile,
        'car': car,
    }
    return render(request, 'car-details.html', context)


def car_edit(request, pk):
    user_profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)
    form = CarForm(instance=car)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect(catalogue_page)
    context = {
        'user_profile': user_profile,
        'form': form,
        'car': car,
    }
    return render(request, 'car-edit.html', context)


def car_delete(request, pk):
    user_profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)
    form = CarDeleteForm(instance=car)
    if request.method == 'POST':
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect(catalogue_page)
    context = {
        'user_profile': user_profile,
        'form': form,
        'car': car,
    }
    return render(request, 'car-delete.html', context)


def profile_create(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    context = {
        'form': form,
    }
    return render(request, 'profile-create.html', context)


def profile_details(request):
    user_profile = Profile.objects.first()
    cars = Car.objects.all()
    cars_price = sum(car.price for car in cars)
    context = {
        'user_profile': user_profile,
        'cars': cars,
        'cars_price': cars_price,
    }
    return render(request, 'profile-details.html', context)


def profile_edit(request):
    user_profile = Profile.objects.first()
    form = ProfileEditForm(instance=user_profile)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect(profile_details)
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    user_profile = Profile.objects.first()
    cars = Car.objects.all()
    form = ProfileDeleteForm(instance=user_profile)
    if request.method == 'POST':
        cars.delete()
        user_profile.delete()
        return redirect(index)
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
