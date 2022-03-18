from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import RegisterCustomUserView, LogoutView


urlpatterns = [
    path('register/', RegisterCustomUserView.as_view(), name = 'register'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name = 'logout'),


]
