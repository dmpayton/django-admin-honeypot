from django.db import models
from admin_honeypot import listeners

class LoginAttempt(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.IPAddressField(blank=True, null=True)
    session_key = models.CharField(max_length=50, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def __unicode__(self):
        return unicode(self.username)
