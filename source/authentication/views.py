from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, permissions, views
from .permissions import RegisterPermission
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .models import CustomUser

from .serializers import CustomUserRegisterSerializer, ProfileSerializer, ChangePasswordSerializer


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

class CustomUserModelViewSet(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            print(self.request.user)
            profile = CustomUser.objects.get(id=request.user.id)
        except CustomUser.DoesNotExist:
            return Response({"data":"Profile doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class UpdatePassword(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get('old_password')
            if not self.object.check_password(old_password):
                return Response({"old_password":['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





