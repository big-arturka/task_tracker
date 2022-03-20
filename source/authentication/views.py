from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, permissions
from .permissions import RegisterPermission
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.views import APIView

from .serializers import CustomUserRegisterSerializer


class RegisterCustomUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [RegisterPermission,]
    serializer_class = CustomUserRegisterSerializer

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'Success':'Success'}, status=status.HTTP_200_OK)





