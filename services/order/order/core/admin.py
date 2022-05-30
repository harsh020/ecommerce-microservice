from django.contrib import admin

from order.core.models import City, State, Country, Address


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    model = City


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    model = State


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    model = Country


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    model = Address
