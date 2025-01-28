from django.shortcuts import render

def index(request):
    template_data = {}
    template_data['title'] = 'Movie Store'
    return render(request, 'home/home.html', {'template_data': template_data})

def about(request):
    return render(request, 'home/about.html')
