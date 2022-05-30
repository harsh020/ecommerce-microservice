from rest_framework import serializers

from api.core.models import Country, State, City


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country',)


class StateSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False, required=False)

    class Meta:
        model = State
        fields = ('state',)


class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer(many=False, required=False)

    class Meta:
        model = City
        fields = ('city',)
