from rest_framework.permissions import BasePermission, SAFE_METHODS

class RegisterPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method != 'GET':
            return True