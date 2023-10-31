from django.apps import AppConfig

class ModifiedUrlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modified_url'
