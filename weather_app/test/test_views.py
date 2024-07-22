# weather_app/tests/test_views.py
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from weather_app.models import City, SearchHistory
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_index_view(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert 'form' in response.context

@pytest.mark.django_db
def test_index_post_view(client):
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    response = client.post(reverse('index'), {'name': 'London'})
    assert response.status_code == 200
    assert 'temperatures' in response.context

@pytest.mark.django_db
def test_search_history_api():
    client = APIClient()
    response = client.get(reverse('search_history_api'))
    assert response.status_code == 200
    assert 'история запросов' in response.json()
