from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        print(dir(view))
        print(request.data)
        print(dir(view.request.data))
        return bool(request.user and view.request.user and view.request.data['cel'])

    def has_object_permission(self, request, view, obj):
        print(obj.user)
        print(request.user)
        return bool(request.user and obj.user and request.user.is_authenticated)