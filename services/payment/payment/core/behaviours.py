from django.db import models
from django.utils.translation import ugettext_lazy as _

class StatusMixin(models.Model):
    is_active = models.BooleanField(_('Is Active'), default=True)
    is_deleted = models.BooleanField(_('Is Deleted'), default=False)

    class Meta:
        abstract = True