from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from admin_honeypot.models import LoginAttempt


class LoginAttemptAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_ip_address', 'get_session_key', 'timestamp', 'get_path')
    list_filter = ('timestamp',)
    readonly_fields = ('path', 'username', 'ip_address', 'session_key', 'user_agent')
    search_fields = ('username', 'ip_address', 'user_agent', 'path')

    def get_actions(self, request):
        actions = super(LoginAttemptAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_session_key(self, instance):
        return '<a href="?session_key=%(key)s">%(key)s</a>' % {'key': instance.session_key}
    get_session_key.short_description = _('Session')
    get_session_key.allow_tags = True

    def get_ip_address(self, instance):
        return '<a href="?ip_address=%(ip)s">%(ip)s</a>' % {'ip': instance.ip_address}
    get_ip_address.short_description = _('IP Address')
    get_ip_address.allow_tags = True

    def get_path(self, instance):
        return '<a href="?path=%(path)s">%(path)s</a>' % {'path': instance.path}
    get_path.short_description = _('URL')
    get_path.allow_tags = True

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(LoginAttempt, LoginAttemptAdmin)
