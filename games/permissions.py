from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method  == "GET" or request.user == obj.purchaser or request.user.id == 1