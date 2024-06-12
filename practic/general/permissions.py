from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        # print(view.request.user)
        # print(request.user)
        return bool(request.user.is_authenticated and view.request.user)

    def has_object_permission(self, request, view, obj):
        # print(obj.user.pk , 'permissions')
        # print(request.user.pk, request.data)
        # print(view.request.user.pk)
        return bool(request.user and obj.user and request.user.is_authenticated)