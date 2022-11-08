from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image_url = models.URLField(null=True)


class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True)
    image = models.URLField(null=True)
    type = models.CharField(max_length=30)
