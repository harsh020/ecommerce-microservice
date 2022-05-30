import json as pyjson

from utils.request.decorator.request_decorator import RequestDecorator


class DictResponseDecorator(RequestDecorator):

    def get(self, url, params=None, **kwargs):
        response = self.request.get(url=url, params=params, **kwargs)
        return pyjson.loads(response.content)

    def post(self, url, data=None, json=None, **kwargs):
        response = self.request.post(url=url, data=data, json=json, **kwargs)
        return pyjson.loads(response.content)

    def patch(self, url, data=None, **kwargs):
        response = self.request.patch(url=url, data=data, **kwargs)
        return pyjson.loads(response.content)

    def put(self, url, data=None, **kwargs):
        response = self.request.put(url=url, data=data, **kwargs)
        return pyjson.loads(response.content)

    def delete(self, **kwargs):
        response = self.request.delete(**kwargs)
        return pyjson.loads(response.content)
