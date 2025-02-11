# Create your views here.
from django.shortcuts import render
from .models import Movie, Review
from django.shortcuts import get_object_or_404, redirect

#Initialize Database

def index(request):
    movies = Movie.objects.all()
    genres = ["Thriller", "Adventure", "Comedy", "Action", "Crime", "Drama", "Romance", "Sci-Fi",
              "War", "Animation", "History", "Family", "Biography", "Western", "Fantasy"]
    return render(request, 'list/listview.html', {'movies': movies, 'genres': genres})

