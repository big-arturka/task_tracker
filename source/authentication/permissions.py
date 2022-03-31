from rest_framework.permissions import SAFE_METHODS, IsAdminUser

class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or request.method == "PATCH" or
            request.user and
            request.user.is_superuser
        )

