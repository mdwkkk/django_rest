from rest_framework import serializers
from .models import Task, Project

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description', 'priority', 'status', 'deadline', 'author', 'executor')

class ProjectSeializer(serializers.ModelSerializer):
    class Meta:
        models = Project
        fields = ('name', 'creator', 'participants')