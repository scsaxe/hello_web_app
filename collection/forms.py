from django.forms import ModelForm
from collection import models


class RestaurantForm(ModelForm):
    class Meta:
        model = models.Restaurant
        fields = ('name', 'description')
