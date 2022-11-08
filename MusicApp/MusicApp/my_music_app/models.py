from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from MusicApp.my_music_app.validators import validate_username


class Profile(models.Model):
    username = models.CharField(max_length=15, validators=[MinLengthValidator(2), validate_username, ])
    email = models.EmailField()
    age = models.PositiveIntegerField(null=True, blank=True)


class Album(models.Model):
    music_genres = [
        ('pop', 'Pop Music'),
        ('jazz', 'Jazz Music'),
        ('r&b', 'R&B Music'),
        ('rock', 'Rock Music'),
        ('country', 'Country Music'),
        ('dance', 'Dance Music'),
        ('hip hop', 'Hip Hop Music'),
        ('other', 'Other'),
    ]
    album_name = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=music_genres)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0.0), ])
