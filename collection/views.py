from django.shortcuts import render, redirect
from collection.forms import RestaurantForm
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


def edit_restaurant(request, slug):
    restaurant = models.Restaurant.objects.get(slug=slug)
    form_class = RestaurantForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_detail', slug=restaurant.slug)

    else:
        form = form_class(instance=restaurant)

    return render(request, 'restaurants/edit_restaurant.html', {
        'restaurant': restaurant,
        'form': form
    })
