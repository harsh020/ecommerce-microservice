from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'api.user'

    def ready(self) -> None:
        import api.user.signals
