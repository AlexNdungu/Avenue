from django.apps import AppConfig


class AvenueshopConfig(AppConfig):
    name = 'avenueShop'

    def ready(self):
        import avenueShop.signals
