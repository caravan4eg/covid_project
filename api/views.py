# TODO откуда брать данные
# TODO посмотреть колины аналоги

from rest_framework import generics
from .models import (
    Fact,
    Location,
    Post,
    Project,
    Photo,
)
from .serializers import (
    FactSerializer,
    LocationSerializer,
    PostSerializer,
    ProjectSerializer,
    PhotoSerializer,
)


class FactList(generics.ListCreateAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer


class FactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
