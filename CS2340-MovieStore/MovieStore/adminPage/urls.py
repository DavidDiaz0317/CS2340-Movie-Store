from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("movies/", views.movies, name="movies"),
    path("users/", views.users, name="users"),
    path("reviews/", views.reviews, name="reviews"),
]