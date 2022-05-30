from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ordering.core import permissions
from ordering.ordering.v1.ordering_strategy.order_handler import OrderHandler
from ordering.ordering.v1.ordering_strategy.order_handler_strategy import EagerOrderHandlerStrategy
from utils.request.decorator.api_key_decorator import ApiKeyDecorator
from utils.request.decorator.dict_response_decorator import DictResponseDecorator
from utils.request.request.request import Request

request_handler = DictResponseDecorator(ApiKeyDecorator(Request()))


class OrderPlaceView(GenericAPIView):
    serializer_class = None
    permission_classes = [permissions.HasApiKey]

    def post(self, request):
        ordering_strategy = EagerOrderHandlerStrategy(request_handler=request_handler)
        order_taking = OrderHandler(ordering_strategy)

        response = order_taking.place_order(request)
        response = {
            'error': False,
            'data': response
        }
        return Response(response, status=status.HTTP_201_CREATED)


class OrderCancelView(GenericAPIView):
    serializer_class = None
    permission_classes = [permissions.HasApiKey]

    def post(self, request):
        ordering_strategy = EagerOrderHandlerStrategy(request_handler=request_handler)
        order_taking = OrderHandler(ordering_strategy)

        response = order_taking.cancel_order(request)
        response = {
            'error': False,
            'message': 'Order cancelled successfully',
            'data': response
        }
        return Response(response, status=status.HTTP_200_OK)


class OrderPaymentUpdateView(GenericAPIView):
    pass