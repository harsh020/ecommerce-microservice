import abc


class IRequest(abc.ABC):
    @abc.abstractmethod
    def get(self, url, params=None, **kwargs):
        raise NotImplemented('Concrete implementation required')

    @abc.abstractmethod
    def post(self, url, data=None, json=None, **kwargs):
        raise NotImplemented('Concrete implementation required')

    @abc.abstractmethod
    def patch(self,url, data=None, **kwargs):
        raise NotImplemented('Concrete implementation required')

    @abc.abstractmethod
    def put(self, url, data=None, **kwargs):
        raise NotImplemented('Concrete implementation required')

    @abc.abstractmethod
    def delete(self, url, **kwargs):
        raise NotImplemented('Concrete implementation required')