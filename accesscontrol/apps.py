from django.apps import AppConfig


class AccesscontrolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accesscontrol'
    def ready(self):
        import accesscontrol.signals    #to make sure that the login and logout are stored in the database correctly
