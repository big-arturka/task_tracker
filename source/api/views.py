from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUserOrReadOnly
from .models import Project, Task, Comment
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer


class ProjectModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = (permissions.IsAdminUser,)
    filter_backends = [SearchFilter]


class TaskModelViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]

class CommentModelViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter]

