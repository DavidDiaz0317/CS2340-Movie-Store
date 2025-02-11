import json

from django.db import models

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

    User = models.CharField(max_length=200)

    Body = models.CharField(max_length=200)

    def __str__(self):
        return self.User

class Order(models.Model):
    User = models.CharField(max_length=200)
    MovieList = models.TextField()
    def set_movielist(self, movies):
        self.MovieList = json.dumps(movies)
    def get_movielist(self):
        return json.loads(self.MovieList) if self.MovieList else []
    def __str__(self):
        return self.MovieList if self.MovieList else ''

