from django.shortcuts import render
from collection import models

def index(request):
    restaurants = models.Restaurant.objects.all()
    return render(request, 'index.html', {
        'restaurants': restaurants,
    })
