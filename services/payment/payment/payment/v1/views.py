from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from payment.core import permissions
from payment.payment.models import Payment
from payment.payment.serializers import PaymentSerializer


class PaymentView(GenericAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.HasApiKey]

    def get(self, request, id=None):
        payment = Payment.objects.get(id=id)
        return Response(self.get_serializer(payment).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        payment, created = Payment.objects.get_or_create(**validated_data)

        return Response(self.get_serializer(payment).data, status=status.HTTP_201_CREATED)

    def patch(self, request, id=None):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance = Payment.objects.get(id=id)
        validated_data = serializer.validated_data
        payment = serializer.update(instance, validated_data)

        return Response(self.get_serializer(payment).data, status=status.HTTP_200_OK)


class PaymentOrderView(GenericAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.HasApiKey]

    def get(self, request, order=None):
        payment = Payment.objects.get(order=order)

        return Response(self.get_serializer(payment).data, status=status.HTTP_200_OK)

    def patch(self, request, order=None):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        instance = Payment.objects.get(order=order)
        validated_data = serializer.validated_data
        payment = serializer.update(instance, validated_data)

        return Response(self.get_serializer(payment).data, status=status.HTTP_200_OK)
