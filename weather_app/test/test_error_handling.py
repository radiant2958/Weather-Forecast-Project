# weather_app/tests/test_error_handling.py
import pytest
from unittest.mock import patch
import requests
from weather_app.views import get_coordinates

@pytest.mark.django_db
@patch('requests.get')
def test_get_coordinates_http_error(mock_get):
    mock_get.side_effect = requests.exceptions.HTTPError
    lat, lng = get_coordinates('London')
    assert lat is None
    assert lng is None

@pytest.mark.django_db
@patch('requests.get')
def test_get_coordinates_connection_error(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError
    lat, lng = get_coordinates('London')
    assert lat is None
    assert lng is None

@pytest.mark.django_db
@patch('requests.get')
def test_get_coordinates_timeout_error(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout
    lat, lng = get_coordinates('London')
    assert lat is None
    assert lng is None

@pytest.mark.django_db
@patch('requests.get')
def test_get_coordinates_invalid_json(mock_get):
    mock_get.return_value.json.side_effect = ValueError
    lat, lng = get_coordinates('London')
    assert lat is None
    assert lng is None
