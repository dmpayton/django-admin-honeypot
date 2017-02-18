import django
import pygeoip
import ipaddress
from admin_honeypot.forms import HoneypotLoginForm
from admin_honeypot.models import LoginAttempt
from admin_honeypot.signals import honeypot
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views import generic
from django.conf import settings


ALLOW_TRACK_ADDRESS = getattr(settings, 'ADMIN_HONEYPOT_ALLOW_TRACK_ADDRESS', True)
PATH_GEOIPV4_CITY = getattr(settings, 'ADMIN_HONEYPOT_PATH_GEOIPV4_CITY', None)
PATH_GEOIPV6_CITY = getattr(settings, 'ADMIN_HONEYPOT_PATH_GEOIPV6_CITY', None)


class AdminHoneypot(generic.FormView):
    template_name = 'admin_honeypot/login.html'
    form_class = HoneypotLoginForm

    def dispatch(self, request, *args, **kwargs):
        if not request.path.endswith('/'):
            return redirect(request.path + '/', permanent=True)

        # Django redirects the user to an explicit login view with
        # a next parameter, so emulate that.
        login_url = reverse('admin_honeypot:login')
        if request.path != login_url:
            return redirect_to_login(request.get_full_path(), login_url)

        return super(AdminHoneypot, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class=form_class):
        return form_class(self.request, **self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        context = super(AdminHoneypot, self).get_context_data(**kwargs)
        path = self.request.get_full_path()
        context.update({
            'app_path': path,
            REDIRECT_FIELD_NAME: reverse('admin_honeypot:index'),
            'title': _('Log in'),
        })
        return context

    def form_valid(self, form):
        return self.form_invalid(form)

    def track_ipaddres(self, ip):
        """
        track detail ip address from client ip.
        return None, if `ALLOW_TRACK_ADDRESS = False` or invalid ipaddress.
        related issue: https://github.com/dmpayton/django-admin-honeypot/issues/41
        """
        if not ALLOW_TRACK_ADDRESS:
            return None

        try:
            ipv_version = ipaddress.ip_address(u'%s' % ip).version
            if ipv_version == 6:
                gi = pygeoip.GeoIP(PATH_GEOIPV6_CITY)
            else:
                gi = pygeoip.GeoIP(PATH_GEOIPV4_CITY)
            return gi.record_by_addr(ip)
        except ValueError:
            # invalid ipv4 or ipv6
            return None

    def form_invalid(self, form):
        instance = LoginAttempt.objects.create(
            username=self.request.POST.get('username'),
            session_key=self.request.session.session_key,
            ip_address=self.request.META.get('REMOTE_ADDR'),
            user_agent=self.request.META.get('HTTP_USER_AGENT'),
            path=self.request.get_full_path(),
            record_by_address=self.track_ipaddres(
                self.request.META.get('REMOTE_ADDR')
            )
        )
        honeypot.send(sender=LoginAttempt, instance=instance, request=self.request)
        return super(AdminHoneypot, self).form_invalid(form)
