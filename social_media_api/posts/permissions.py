from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit/delete it.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are GET, HEAD, OPTIONS → always allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the author can edit/delete
        return obj.author == request.user
