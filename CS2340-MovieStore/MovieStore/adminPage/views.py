from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the adminpage index.")
def movies(request):
    return HttpResponse("Hello, world. You're at the movies page.")
def users(request):
    return HttpResponse("Hello, world. You're at the user page.")
def reviews(request):
    return HttpResponse("Hello, world. You're at the reviews.")
