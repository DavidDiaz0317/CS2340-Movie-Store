# Create your views here.
from django.shortcuts import render
from django.conf import settings
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#Initialize Database
cred = credentials.Certificate(settings.SERVICE_KEY_PATH)
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
