from django.conf import settings

from utils.request.decorator.request_decorator import RequestDecorator


class ApiKeyDecorator(RequestDecorator):
    def _modify_headers(self, **kwargs):
        headers = kwargs.get('headers', dict())
        headers['X-Api-Key'] = settings.API_KEY
        kwargs['headers'] = headers
        return kwargs

    def get(self, url, params=None, **kwargs):
        kwargs = self._modify_headers(**kwargs)
        return self.request.get(url=url, params=params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        kwargs = self._modify_headers(**kwargs)
        return self.request.post(url=url, data=data, json=json, **kwargs)

    def patch(self, url, data=None, **kwargs):
        kwargs = self._modify_headers(**kwargs)
        return self.request.patch(url=url, data=data, **kwargs)

    def put(self, url, data=None, **kwargs):
        kwargs = self._modify_headers(**kwargs)
        return self.request.put(url=url, data=data, **kwargs)

    def delete(self, **kwargs):
        kwargs = self._modify_headers(**kwargs)
        return self.request.delete(**kwargs)
