from ipware import get_client_ip

from django.contrib.admin import AdminSite
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import generic

from admin_honeypot.forms import HoneypotLoginForm
from admin_honeypot.models import LoginAttempt
from admin_honeypot.signals import honeypot


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

        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=form_class):
        return form_class(self.request, **self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        path = self.request.get_full_path()
        admin_site = AdminSite()
        context.update({
            'app_path': path,
            REDIRECT_FIELD_NAME: reverse('admin_honeypot:index'),
            'title': _('Log in'),
            'site_title': admin_site.site_title,
            'site_header': admin_site.site_header,
            'username': self.request.user.get_username(),
        })
        return context

    def form_valid(self, form):
        return self.form_invalid(form)

    def form_invalid(self, form):
        ip, is_routable = get_client_ip(self.request)

        instance = LoginAttempt.objects.create(
            username=self.request.POST.get('username'),
            session_key=self.request.session.session_key,
            ip_address=ip,
            user_agent=self.request.META.get('HTTP_USER_AGENT'),
            path=self.request.get_full_path(),
        )
        honeypot.send(sender=LoginAttempt, instance=instance, request=self.request)
        return super().form_invalid(form)
