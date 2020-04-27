# api/serializers.py
from rest_framework import serializers
from .models import Fact, Location, Post, Project, Image


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('created_at', 'updated_at',)
        model = Fact


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Location


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Post


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Project


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Image
