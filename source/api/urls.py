from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectModelViewSet, TaskModelViewSet


router = DefaultRouter()
router.register(r'^', ProjectModelViewSet, basename='project')
router.register(r'^task', TaskModelViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]



