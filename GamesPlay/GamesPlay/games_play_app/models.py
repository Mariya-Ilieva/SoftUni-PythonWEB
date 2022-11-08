from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    email = models.EmailField()
    age = models.PositiveIntegerField(validators=[MinValueValidator(12), ])
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)


class Game(models.Model):
    GAME_TYPES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),

    ]
    title = models.CharField(max_length=30, unique=True)
    category = models.CharField(max_length=15, choices=GAME_TYPES)
    rating = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(0.5), ])
    max_level = models.PositiveIntegerField(validators=[MinValueValidator(1), ], null=True, blank=True)
    image_url = models.URLField()
    summary = models.TextField(null=True, blank=True)
