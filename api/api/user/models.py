from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

from api.core.behaviours import StatusMixin, ProfileMixin, PhoneMixin


class User(AbstractUser):
    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def __str__(self):
        return self.username


class UserProfile(StatusMixin, TimeStampedModel, ProfileMixin, PhoneMixin):
    user = models.OneToOneField(User, blank=True, null=True,
                                on_delete=models.CASCADE, related_name='user_profile')

    def __str__(self):
        return self.user.username
