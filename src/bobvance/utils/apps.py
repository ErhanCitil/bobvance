from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "bobvance.utils"

    def ready(self):
        from . import checks  # noqa
