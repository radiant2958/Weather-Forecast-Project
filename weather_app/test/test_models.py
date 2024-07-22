# weather_app/tests/test_models.py
import pytest
from django.contrib.auth.models import User
from weather_app.models import City, SearchHistory

@pytest.mark.django_db
def test_city_str():
    city = City(name='London')
    assert str(city) == 'London'

@pytest.mark.django_db
def test_search_history_str():
    user = User.objects.create_user(username='testuser', password='12345')
    city = City.objects.create(name='London')
    search_history = SearchHistory.objects.create(user=user, city=city)
    assert str(search_history) == 'testuser - London'
