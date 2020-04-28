# api/urls.py
from django.urls import path
from .views import (
    ApiRoot,
    FactList,
    FactDetail,
    PostList,
    ProjectList,

)

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('<int:pk>/', FactDetail.as_view(), name=FactDetail.name),
    path('facts/', FactList.as_view(), name=FactList.name),
    path('posts/', PostList.as_view(), name=PostList.name),
    path('projects/', ProjectList.as_view(), name=ProjectList.name),

]
