import json

from rest_framework import status
from rest_framework.generics import GenericAPIView
from django.conf import settings
from rest_framework.response import Response

from cart.core import permissions


class CartView(GenericAPIView):
    permission_classes = [permissions.HasApiKey]

    def get(self, request, customer=None):
        cart = settings.REDIS.get(customer)
        if cart is None:
            cart = '{}'
            settings.REDIS.set(customer, cart)
        response = {
            'error': False,
            'data': json.loads(cart)
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, customer=None):
        cart = json.dumps(request.data)
        settings.REDIS.set(customer, cart)

        response = {
            'error': False,
            'data': json.loads(cart)
        }
        return Response(response, status=status.HTTP_201_CREATED)

    def put(self, request, customer=None):
        cart = json.dumps(request.data)

        settings.REDIS.set(customer, cart)
        response = {
            'error': False,
            'data': json.loads(cart)
        }
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, customer=None):
        cart = settings.REDIS.get(customer)
        if cart:
            settings.REDIS.delete(customer)

        response = {
            'error': False,
            'message': 'Cart cleared successfully'
        }
        return Response(response, status=status.HTTP_205_RESET_CONTENT)




