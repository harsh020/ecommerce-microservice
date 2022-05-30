from django.db.models.signals import pre_save
from api.user.models import User


def update_user(sender, instance, **kwargs):
    user = instance
    if user.email != '':
        user.username = user.email
    if user.name != '':
        names = user.name.split(' ')
        user.first_name = names[0]
        user.last_name = ' '.join(names[1:])


pre_save.connect(update_user, sender=User)