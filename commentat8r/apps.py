from django.contrib.admin.apps import AdminConfig


class Commentat8rAdminConfig(AdminConfig):
    default_site = 'admin.Commentat8rAdminSite'
    default_auto_field = 'django.db.models.BigAutoField'
