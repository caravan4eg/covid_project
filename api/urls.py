# api/urls.py
from django.urls import path
from .views import FactList, FactDetail

urlpatterns = [
    path('<int:pk>/', FactDetail.as_view()),
    path('', FactList.as_view()),
    path('', FactList.as_view()),

]
