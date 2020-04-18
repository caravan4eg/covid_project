# TODO откуда брать данные
# TODO посмотреть колины аналоги

from rest_framework import generics
from .models import Fact
from .serializers import FactSerializer


class FactList(generics.ListCreateAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer


class FactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer
