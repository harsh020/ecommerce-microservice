from django.db import models
from django.utils.translation import ugettext_lazy as _

from order.core.behaviours import PhoneMixin


class Country(models.Model):
    country = models.CharField(_('Country'), max_length=100, blank=True, null=True)

    def __str__(self):
        return self.country


class State(models.Model):
    state = models.CharField(_('State'), max_length=100, blank=True, null=True)
    country = models.ForeignKey('core.Country', on_delete=models.CASCADE, blank=True, null=True, related_name='country_state')

    def __str__(self):
        return self.state


class City(models.Model):
    city = models.CharField(_('City'), max_length=100, blank=True, null=True)
    state = models.ForeignKey('core.State', on_delete=models.CASCADE, blank=True, null=True, related_name='state_city')

    def __str__(self):
        return self.city


class Address(PhoneMixin):
    full_name = models.CharField(_("Full Name"), max_length=100, blank=True, null=True)
    house_number = models.CharField(_("House Number"), max_length=20, blank=True, null=True)
    area = models.CharField(_("Area"), max_length=50, blank=True, null=True)
    landmark = models.CharField(_("Landmark"), max_length=50, blank=True, null=True)
    pincode = models.CharField(_("Pincode"), max_length=6, blank=True, null=True)

    city = models.ForeignKey('core.City', on_delete=models.CASCADE, related_name='city_address')
    state = models.ForeignKey('core.State', on_delete=models.CASCADE, related_name='state_address')
    country = models.ForeignKey('core.Country', on_delete=models.CASCADE, related_name='country_address')
