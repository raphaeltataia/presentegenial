from rest_framework.permissions import BasePermission
from ..models import Campaign


class IsOwner(BasePermission):
    """Custom permission class to allow only campaign owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the campaign owner."""
        if isinstance(obj, Campaign):
            return obj.user == request.user
        return obj.user == request.user


class IsPostOrIsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'POST':
            return True

        # Otherwise, only allow authenticated requests
        return request.user and request.user.is_authenticated()