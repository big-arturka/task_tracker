from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status, permissions, views, viewsets
from .permissions import IsAdminUserOrReadOnly
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .models import CustomUser
from django.shortcuts import get_object_or_404
from .serializers import CustomUserRegisterSerializer, ChangePasswordSerializer
from rest_framework.filters import SearchFilter


class CustomUserModelViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserRegisterSerializer
    queryset = CustomUser.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = [SearchFilter]

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

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'Success':'Success'}, status=status.HTTP_200_OK)





