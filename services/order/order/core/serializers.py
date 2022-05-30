from rest_framework import serializers

from order.core.models import Country, City, State, Address


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country',)


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('state',)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city',)


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'
