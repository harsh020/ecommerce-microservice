import json as pyjson
from rest_framework.response import Response

from utils.request.decorator.request_decorator import RequestDecorator


class DRFResponseDecorator(RequestDecorator):

    def get(self, url, params=None, **kwargs):
        response = self.request.get(url=url, params=params, **kwargs)
        return Response(pyjson.loads(response.content), status=response.status_code)

    def post(self, url, data=None, json=None, **kwargs):
        response = self.request.post(url=url, data=data, json=json, **kwargs)
        return Response(pyjson.loads(response.content), status=response.status_code)

    def patch(self, url, data=None, **kwargs):
        response = self.request.patch(url=url, data=data, **kwargs)
        return Response(pyjson.loads(response.content), status=response.status_code)

    def put(self, url, data=None, **kwargs):
        response = self.request.put(url=url, data=data, **kwargs)
        return Response(pyjson.loads(response.content), status=response.status_code)

    def delete(self, **kwargs):
        response = self.request.delete(**kwargs)
        return Response(pyjson.loads(response.content), status=response.status_code)
