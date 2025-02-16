import json

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Movie(models.Model):

    id = models.AutoField(primary_key=True)

    Title = models.CharField(max_length=200)

    Plot = models.CharField(max_length=400)

    Director = models.CharField(max_length=200)

    Genre = models.CharField(max_length=200)

    Poster = models.CharField(max_length=200)

    Year = models.CharField(max_length=4)

    Price = models.IntegerField(default=10)

    def __str__(self):
        return self.Title

class Review(models.Model):
    id = models.AutoField(primary_key=True)

    comment = models.CharField(max_length=255, blank=True, null=True)

    date = models.DateField(auto_now=True)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.movie.Title


