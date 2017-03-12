from django.db import models


class Airport(models.Model):
    identifier = models.CharField(max_length=4, unique=True)
    name = models.TextField()
    latitude = models.DecimalField(decimal_places=10, max_digits=13)
    longitude = models.DecimalField(decimal_places=10, max_digits=13)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    perdiem_rate = models.IntegerField(null=True)
