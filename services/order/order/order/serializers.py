from rest_framework import serializers

from order.core.serializers import AddressSerializer
from order.order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ('is_active', 'is_deleted', 'created', 'modified', 'order')


class OrderSerializer(serializers.ModelSerializer):
    shipping_address = AddressSerializer(many=False, partial=True)
    order_items = OrderItemSerializer(many=True, partial=True)

    def get_by_id(self, id):
        return Order.objects.get(id=id)

    class Meta:
        model = Order
        fields = '__all__'
