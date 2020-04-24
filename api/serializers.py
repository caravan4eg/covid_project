# api/serializers.py
from rest_framework import serializers
from .models import Fact, Location, Post, Project, Photo


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
        exclude = ('updated_at',)
        model = Post


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('author', 'updated_at')
        model = Project


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('updated_at',)
        model = Photo
