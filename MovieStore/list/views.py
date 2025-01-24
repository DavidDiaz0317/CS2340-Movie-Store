# Create your views here.
from django.shortcuts import render
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Replace with the path to your service account key file
cred = credentials.Certificate("C:\\Users\\david\\PycharmProjects\\CS2340-MovieStore\\MovieStore\\service_key.json")
firebase_admin.initialize_app(cred)




def index(request):
    db = firestore.client()
    MOVIES_REF = db.collection('Movies')
    docs = MOVIES_REF.stream()
    movies = []
    i = 0
    for doc in docs:
        movies.append(doc.to_dict())
    return render(request, 'list/listview.html', {'movies': movies})
