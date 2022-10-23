from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    # remove, just for demo.
    def ready(self) -> None:
        import core.signals.handlers
