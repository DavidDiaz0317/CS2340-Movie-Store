from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.admin_home, name="admin_home"),
    path("movies/", views.admin_movies, name="admin_movies"),
    path("reviews/", views.admin_reviews, name="admin_reviews"),

    #user management
    path("users/", views.admin_users, name="admin_users"),
    path('create/', views.create_user, name="create_user"),
    path('edit/<int:user_id>/', views.edit_user, name="edit_user"),
    path('delete/<int:user_id>/', views.delete_user, name="delete_user"),
]