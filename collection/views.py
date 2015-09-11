from django.shortcuts import render
from collection import models


def index(request):
    restaurants = models.Restaurant.objects.all()
    return render(request, 'index.html', {
        'restaurants': restaurants,
    })


def restaurant_detail(request, slug):
    restaurant = models.Restaurant.objects.get(slug=slug)
    return render(request, 'restaurants/restaurant_detail.html',
                  {'restaurant': restaurant})
