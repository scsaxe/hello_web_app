from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(unique=True)
