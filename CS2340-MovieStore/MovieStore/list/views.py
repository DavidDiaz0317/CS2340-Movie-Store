# Create your views here.
from django.shortcuts import render, redirect
from .models import Movie, Review
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

#Initialize Database

def index(request):
    movies = Movie.objects.all()
    genres = ["Thriller", "Adventure", "Comedy", "Action", "Crime", "Drama", "Romance", "Sci-Fi",
              "War", "Animation", "History", "Family", "Biography", "Western", "Fantasy"]
    return render(request, 'list/listview.html', {'movies': movies, 'genres': genres})

@login_required
def create_review(request, id):
    if request.method == 'POST' and request.POST['comment'] != '':
        movie = Movie.objects.get(id=id)
        review = Review()
        review.comment = request.POST['comment']
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movies.index', id=id)
    else:
        return redirect('movies.index', id=id)