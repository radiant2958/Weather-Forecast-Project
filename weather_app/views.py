from django.shortcuts import render
from django.http import JsonResponse
from .models import City, SearchHistory
from .forms import CityForm
import requests
from django.db.models import Count
import json
import logging

logger = logging.getLogger(__name__)

def get_coordinates(city_name):
    try:
        response = requests.get(f'https://api.opencagedata.com/geocode/v1/json?q={city_name}&key=b4b8c0c799df49ccb51391fd640cfc3a')
        response.raise_for_status()  
        data = response.json()
        logger.debug(f"Response from OpenCageData: {data}")
        if 'results' in data and data['results']:
            coordinates = data['results'][0]['geometry']
            return coordinates['lat'], coordinates['lng']
        return None, None
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, ValueError) as e:
        logger.error(f"Ошибка при получении координат для {city_name}: {e}")
        return None, None




def index(request):
    weather_data = None
    temperatures = None
    last_searched_city = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            city, created = City.objects.get_or_create(name=city_name)
            if request.user.is_authenticated:
                SearchHistory.objects.create(user=request.user, city=city)
            last_searched_city = city_name

            coordinates = get_coordinates(city_name)
            logger.debug(f"Coordinates for {city_name}: {coordinates}")
            if coordinates:
                latitude, longitude = coordinates
                response = requests.get(
                    f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,cloudcover_mean&timezone=Europe%2FLondon'
                )
                logger.debug(f"Запрос к Open Meteo: {response.url}")
                logger.debug(f"Статус ответа: {response.status_code}")
                if response.status_code == 200:
                    weather_data = response.json()
                    logger.debug(f"Данные о погоде для {city_name}: {weather_data}")

                    if 'daily' in weather_data:
                        temperatures = zip(
                            weather_data['daily']['time'],
                            weather_data['daily']['temperature_2m_max'],
                            weather_data['daily']['temperature_2m_min'],
                            weather_data['daily']['precipitation_sum'],
                            weather_data['daily']['cloudcover_mean']
                        )
                    else:
                        logger.error(f"Ключ 'daily' не найден в weather_data для {city_name}")
                else:
                    logger.error(f"Ошибка запроса к Open Meteo: {response.text}")
    else:
        form = CityForm()

    return render(request, 'weather_app/index.html', {
        'form': form,
        'temperatures': temperatures,
        'last_searched_city': last_searched_city
    })


def search_history_api(request):
    search_history = SearchHistory.objects.values('city__name').annotate(count=Count('city__name'))
    search_history_list = list(search_history)
    return JsonResponse({"история запросов": search_history_list}, json_dumps_params={'ensure_ascii': False})

