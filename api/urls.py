# api/urls.py
from django.urls import path
from .views import (
    FactList,
    FactDetail,
    LocationList,
    PostList,
    ProjectList,
    PhotoViewSet,
)

# img_router = DefaultRouter()
# img_router.register(r'img', PhotoViewSet)

urlpatterns = [
    path('<int:pk>', FactDetail.as_view(), name=FactDetail.name),
    path('facts', FactList.as_view(), name=FactList.name),
    path('locations', LocationList.as_view(), name=LocationList.name),
    path('posts', PostList.as_view(), name=FactList.name),
    path('projects', ProjectList.as_view(), name=ProjectList.name),
    path('photos', PhotoViewSet, name=PhotoViewSet.name),


]
