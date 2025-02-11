from django.urls import path
from . import views

urlpatterns = [

path('', views.index, name='cart.index'),
path('add/<int:id>/', views.add, name='cart.add'),

path('clear/', views.clear, name='cart.clear'),
]