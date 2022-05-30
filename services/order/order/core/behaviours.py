from django.db import models
from django.utils.translation import ugettext_lazy as _


class StatusMixin(models.Model):
    is_active = models.BooleanField(_('is_active'), blank=True, null=True, default=True)
    is_deleted = models.BooleanField(_('is_deleted'), blank=True, null=True, default=False)

    class Meta:
        abstract = True


class PhoneMixin(models.Model):
    phone_number = models.CharField(_('Phone Number'), max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
