import requests

from .request_interface import IRequest


class Request(IRequest):

    def get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return requests.post(url=url, data=data, json=json, **kwargs)

    def patch(self,url, data=None, **kwargs):
        return requests.patch(url=url, data=data, **kwargs)

    def put(self, url, data=None, **kwargs):
        return requests.put(url=url, data=data, **kwargs)

    def delete(self, url, **kwargs):
        return requests.delete(url=url, **kwargs)