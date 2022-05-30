from django.conf import settings
from rest_framework.generics import GenericAPIView

from api.core import permissions
from utils.request.decorator.api_key_decorator import ApiKeyDecorator
from utils.request.decorator.drf_response_decorator import DRFResponseDecorator
from utils.request.request.request import Request

request_handler = DRFResponseDecorator(ApiKeyDecorator(Request()))


class ProxyView(GenericAPIView):
    serializer_class = None
    permission_classes = [permissions.IsAuthenticatedOrSafeServiceReadOnly]

    def _create_url(self, url):
        # Take url index at 1 bcs here the leading / is removed by django as opposed to permissions
        service = url.split('/')[1].upper()
        base_url = settings.EXTERNAL_SERVICES[service]
        url = f'{base_url}/{url}'

        return url

    def post(self, request, url=None):
        url = self._create_url(url)
        return request_handler.post(url=url, json=request.data)

    def get(self, request, url=None):
        url = self._create_url(url)
        return request_handler.get(url=url, params=request.GET)

    def patch(self, request, url=None):
        url = self._create_url(url)
        return request_handler.patch(url=url, json=request.data)

    def put(self, request, url=None):
        url = self._create_url(url)
        return request_handler.put(url=url, json=request.data)

    def delete(self, request, url=None):
        url = self._create_url(url)
        return request_handler.delete(url=url)
