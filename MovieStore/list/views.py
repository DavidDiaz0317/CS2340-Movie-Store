from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('list/listview.html')
    return HttpResponse(template.render())
