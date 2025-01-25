# Create your views here.
from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#Initialize Database
cred = credentials.Certificate("C:\\Users\\david\\PycharmProjects\\CS2340-MovieStore\\MovieStore\\service_key.json")
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
