from utils.request.request.request import IRequest


class RequestDecorator(IRequest):
    def __init__(self, request: IRequest) -> None:
        self.request = request

    def get(self, url, params=None, **kwargs):
        return self.request.get(url=url, params=params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request.post(url=url, data=data, json=json, **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request.patch(url=url, data=data, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request.put(url=url, data=data, **kwargs)

    def delete(self, **kwargs):
        return self.request.delete(**kwargs)
