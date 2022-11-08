from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from car_collection.car_collection_app.validators import validate_username, validate_year


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[validate_username, ])
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), ])
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Last Name')
    profile_picture = models.URLField(null=True, blank=True, verbose_name='Profile Picture')


class Car(models.Model):
    CAR_TYPES = [
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES)
    model = models.CharField(max_length=20, validators=[MinLengthValidator(2), ])
    year = models.IntegerField(validators=[validate_year, ])
    image_url = models.URLField(verbose_name='Image URL')
    price = models.FloatField(validators=[MinValueValidator(1.0), ])
