from django.db import models
from django.utils.translation import ugettext_lazy as _

from api import core


class StatusMixin(models.Model):
    is_active = models.BooleanField(_('is_active'), blank=True, null=True, default=True)
    is_deleted = models.BooleanField(_('is_deleted'), blank=True, null=True, default=False)

    class Meta:
        abstract = True


class PhoneMixin(models.Model):
    country_code = models.CharField(_('Country Code'), max_length=4, blank=True, null=True)

    # TODO: Add phone number validator
    mobile = models.CharField(_('Mobile No'), max_length=10, blank=True, null=True)

    class Meta:
        abstract = True


class AddressMixin(models.Model):
    address = models.CharField(_("Address"), max_length=100, blank=True, null=True)
    country = models.ForeignKey("core.Country", models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey("core.State", models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey("core.City", models.SET_NULL, blank=True, null=True)
    pincode = models.CharField(_("Pincode"), max_length=10, blank=True, null=True)

    class Meta:
        abstract = True


class ProfileMixin(models.Model):
    date_of_birth = models.DateField(blank=True, null=True)

    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, null=True)

    class Meta:
        abstract = True

