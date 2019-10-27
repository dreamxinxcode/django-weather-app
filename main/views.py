from django.shortcuts import render
from .models import Cities
import requests
# Create your views here.


def homepage_view(request):
    api_key = "e0d88f84620009644667c282466ed877"
    cities = Cities.objects.all()

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city, api_key)).json()

        city_weather = {
            'city': city.name,
            'temp': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {
        "title": "Django Weather App",
        "weather_data": weather_data,
    }
    return render(request, "main/index.html", context)


def about_view(request):

    context = {
        "title": "Django Weather App | About",
    }
    return render(request, "main/about.html", context)


def contact_view(request):
    context = {
        "title": "Django Weather App | Contact",
    }
    return render(request, "main/contact.html", context)