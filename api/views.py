# TODO откуда брать данные
# TODO посмотреть колины аналоги
# TODO загрузка фото
# TODO make mockup like https://news.google.com/covid19/map?hl=ru&gl=RU&ceid=RU:ru

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse

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
    name = 'factlist'


class FactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer
    name = 'factdetail'


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    name = 'locationlist'


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'postlist'


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    name = 'projectlist'


class PhotoViewSet(viewsets.ModelViewSet):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    name = 'photoviewset'


class ApiRoot(generics.GenericAPIView):
    name = 'CovidMonitor API-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'projectlist': reverse(ProjectList.name, request=request),
            'postlist': reverse(PostList.name, request=request),
            'locationlist': reverse(LocationList.name, request=request),
            'factlist': reverse(FactList.name, request=request),
        })
