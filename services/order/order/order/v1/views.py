from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from order.core import permissions
from order.core.models import Address
from order.order.models import Order, OrderItem
from order.order.serializers import OrderSerializer


class OrderCreateView(GenericAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.HasApiKey]

    def post(self, request):
        # print(request.data)
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        shipping_address = validated_data.pop('shipping_address')
        order_items = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        order.shipping_address, created = Address.objects.get_or_create(**shipping_address)

        for order_item in order_items:
            order_item = OrderItem.objects.create(**order_item)
            order_item.order = order
            order_item.save()
        order.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class OrderDetailView(GenericAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.HasApiKey]

    def get(self, request, id=None):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class()
        instance = serializer.get_by_id(id)

        return Response(serializer_class(instance).data, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        serializer.is_valid()

        validated_data = serializer.validated_data
        instance = Order.objects.get(id=id)
        instance = serializer.update(instance, validated_data)

        return Response(serializer_class(instance).data, status=status.HTTP_200_OK)


class OrderListView(GenericAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.HasApiKey]
    queryset = Order.objects.all()

    def get(self, request, id=None):
        serializer_class = self.get_serializer_class()
        instances = self.get_queryset().filter(customer=id)

        return Response(serializer_class(instances, many=True, read_only=True).data, status=status.HTTP_200_OK)


class OrderAdminView(GenericAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.HasApiKey]
    queryset = Order.objects.all()

    def get(self, request):
        serializer_class = self.get_serializer_class()
        instances = self.get_queryset()

        return Response(serializer_class(instances, many=True).data, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, partial=True)
        serializer.is_valid()

        validated_data = serializer.validated_data
        instance = Order.objects.get(id=id)
        serializer.update(instance, validated_data)

        return Response(serializer_class(instance).data, status=status.HTTP_200_OK)