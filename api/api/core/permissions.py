from django.conf import settings
from django.urls import reverse
from rest_framework import permissions

SAFE_METHODS = ['GET']
SAFE_SERVICES = settings.SAFE_SERVICES


class IsAuthenticatedOrSafeServiceReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Take url index at 2 bcs here the leading / is not removed by django as opposed to proxy view
        service = request.get_full_path().split('/')[2].upper()

        return (
            (request.user and request.user.is_authenticated) or
            (request.method in SAFE_METHODS and service in SAFE_SERVICES)
        )
