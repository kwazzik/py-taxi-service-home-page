from django.http import HttpRequest
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest):
    num_drivers = Driver.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()
    num_cars = Car.objects.all().count()
    return render(request, "taxi/index.html", context={
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    })
