from rest_framework.viewsets import ModelViewSet

from .models import Fact, Post, Project
from .serializers import FactSerializer, PostSerializer, ProjectSerializer

# JWT Auth
from rest_framework.permissions import IsAuthenticated


class FactViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Fact.objects.all()
    serializer_class = FactSerializer


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ProjectViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
