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

def show(request, id):
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie)
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()

    template_data = {}
    template_data['title'] = movie.Title
    template_data['movie'] = movie
    template_data['reviews'] = reviews
    template_data['user_review'] = user_review
    return render(request, 'list/show.html', {'template_data' : template_data})

@login_required
def create_review(request, id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=id)
        if request.POST.get('comment'):
            review = Review()
            review.comment = request.POST['comment']
            review.movie = movie
            review.user = request.user
            review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)

def edit_review(request, id, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.user != review.user:
        return redirect('movies.show', id=review.id)
    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Review'
        template_data['review'] = review
        return render(request, 'list/edit_review.html', {'template_data' : template_data})
    elif request.method == 'POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)

def delete_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    return redirect('movies.show', id=id)