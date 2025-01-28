# Create your views here.
from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("C:\\Users\\david\\PycharmProjects\\CS2340-MovieStore\\MovieStore\\service_key.json")
firebase_admin.initialize_app(cred)




def index(request):
    db = firestore.client()
    MOVIES_REF = db.collection('Movies')
    genres = ["Thriller", "Adventure", "Comedy", "Action", "Crime", "Drama", "Romance", "Sci-Fi", "War", "Animation", "History", "Family", "Biography", "Western", "Fantasy"]
    docs = MOVIES_REF.stream()
    movies = []
    i = 0
    for doc in docs:
        movies.append(doc.to_dict())
    return render(request, 'list/listview.html', {'movies': movies, 'genres': genres})
