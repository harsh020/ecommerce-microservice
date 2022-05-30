from django.conf import settings
from rest_framework import permissions


class HasApiKey(permissions.BasePermission):
    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_X_API_KEY')
        return api_key == settings.API_KEY
