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

    #Open Database
    db = firestore.client()

    #Store movies from database in a dictionary
    MOVIES_REF = db.collection('Movies')
    docs = MOVIES_REF.stream()
    movies = []
    for doc in docs:
        movies.append(doc.to_dict())

    #Render list site
    return render(request, 'list/listview.html', {'movies': movies})
