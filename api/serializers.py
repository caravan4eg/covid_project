# api/serializers.py
from rest_framework import serializers
from .models import Fact, Location


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('author', 'updated_at')
        model = Fact


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Location
