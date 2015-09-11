from django.contrib import admin

from collection.models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Restaurant, RestaurantAdmin)
