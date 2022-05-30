from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'payment.user'

    def ready(self) -> None:
        import payment.user.signals
