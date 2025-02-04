from django.db import models

# Create your models here.

class Movie(models.Model):
    Title = models.CharField(max_length=200)

    Plot = models.CharField(max_length=400)

    Director = models.CharField(max_length=200)

    Genre = models.CharField(max_length=200)

    Poster = models.CharField(max_length=200)

    Year = models.CharField(max_length=4)


    def __str__(self):
        return self.Title

