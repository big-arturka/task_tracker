from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectModelViewSet, TaskModelViewSet, CommentModelViewSet


router = DefaultRouter()
router.register(r'^task', TaskModelViewSet, basename='task')
router.register(r'^comment', CommentModelViewSet, basename='comment')
router.register(r'', ProjectModelViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]



