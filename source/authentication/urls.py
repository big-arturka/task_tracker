from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import LogoutView, CustomUserModelViewSet, UpdatePassword


router = DefaultRouter()
router.register(r'profile', CustomUserModelViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('change-password/', UpdatePassword.as_view(), name = 'change-password'),


]
