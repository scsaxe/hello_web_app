from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
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


@login_required
def edit_restaurant(request, slug):
    restaurant = models.Restaurant.objects.get(slug=slug)
    if restaurant.user != request.user:
        raise Http404

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


def create_restaurant(request):
    form_class = RestaurantForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.user = request.user
            restaurant.slug = slugify(restaurant.name)
            restaurant.save()
            return redirect('restaurant_detail', slug=restaurant.slug)
    else:
        form = form_class()

    return render(request, 'restaurants/create_restaurant.html', {
        'form': form,
    })
