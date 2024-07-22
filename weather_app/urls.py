from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/search-history/', views.search_history_api, name='search_history_api'),
]
