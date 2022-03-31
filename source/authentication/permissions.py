from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser, AllowAny

class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or request.method == "PATCH" or
            request.user and
            request.user.is_superuser
        )

