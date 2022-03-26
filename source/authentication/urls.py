from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import RegisterCustomUserView, LogoutView, CustomUserModelViewSet, UpdatePassword


urlpatterns = [
    path('register/', RegisterCustomUserView.as_view(), name = 'register'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('profile/', CustomUserModelViewSet.as_view(), name = 'profile'),
    path('change-password/', UpdatePassword.as_view(), name = 'change-password'),


]
