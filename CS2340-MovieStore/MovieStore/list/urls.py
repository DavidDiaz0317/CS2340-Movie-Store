from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path("", views.index, name="movies.index"),
    path('<int:id>/review/create/', views.create_review,name='movies.create_review'),
]



