from rest_framework import permissions
from .models import *

class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.type in ('owner', 'admin')
