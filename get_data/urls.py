# api/urls.py
from django.urls import path
from .views import HomePageView, demo

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('demo/', demo),
]
