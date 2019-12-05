from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthConfig(AppConfig):
    name = 'admin_honeypot'
    verbose_name = _("Admin Honeypot")
