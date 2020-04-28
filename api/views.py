# TODO откуда брать данные
# TODO посмотреть колины аналоги
# TODO загрузка фото?


from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import (
    Fact,
    Post,
    Project
)
from .serializers import (
    FactSerializer,
    PostSerializer,
    ProjectSerializer,
)


class FactList(generics.ListCreateAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer
    name = 'factlist'


class FactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer
    name = 'factdetail'

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.order_by('-published_at')
    serializer_class = PostSerializer
    name = 'postlist'


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    name = 'projectlist'


class ApiRoot(generics.GenericAPIView):
    name = 'CovidMonitor API-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'projectlist': reverse(ProjectList.name, request=request),
            'postlist': reverse(PostList.name, request=request),
            'factlist': reverse(FactList.name, request=request),
        })
