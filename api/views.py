from rest_framework.viewsets import ModelViewSet

from .models import Fact, Post, Project
from .serializers import FactSerializer, PostSerializer, ProjectSerializer


class FactViewSet(ModelViewSet):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
