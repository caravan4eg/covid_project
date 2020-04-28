# api/serializers.py
from rest_framework import serializers
from .models import Fact, Post, Project


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Post


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Project
