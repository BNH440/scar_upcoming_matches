from django.apps import AppConfig


class FightConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fights"

    def ready(self):
        import fights.signals  # Import the signals module

        from . import auto_refresh
        auto_refresh.start_auto_refresh()
