from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, status
from rest_framework import permissions
from .permissions import IsAdminUserOrReadOnly
from .models import Project, Task, Comment, Action
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer
from rest_framework.response import Response
from .services import action_create


class ProjectModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [SearchFilter]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = request.user
        project = serializer.instance
        text = f"{user.first_name} created project '{project.name}'"
        action_create(user=user, text=text, project=project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        user = request.user
        project = serializer.instance
        text = f"{user.first_name} updated project '{project.name}'"
        action_create(user=user, text=text, project=project)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        project = self.get_object()
        text = f"{user.first_name} deleted project '{project.name}'"
        action_create(user=user, text=text)
        self.perform_destroy(project)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskModelViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    filter_backends = [SearchFilter]


class CommentModelViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter]

