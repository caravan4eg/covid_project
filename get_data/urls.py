# api/urls.py
from django.urls import path
from .views import HomePageView, BlogPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog', BlogPageView.as_view(), name='blog'),
]
