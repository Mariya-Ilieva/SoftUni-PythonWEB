from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    image_url = models.URLField(null=False, blank=False)


class Note(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    image_url = models.URLField(null=False, blank=False)
    content = models.TextField(null=False, blank=False)
