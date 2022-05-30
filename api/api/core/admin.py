from django.contrib import admin

# Register your models here.
from api.core.models import Country, City, State


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    model = Country


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    model = City


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    model = State