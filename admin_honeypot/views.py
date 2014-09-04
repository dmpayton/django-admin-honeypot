import django
from admin_honeypot.forms import HoneypotLoginForm
from admin_honeypot.models import LoginAttempt
from admin_honeypot.signals import honeypot
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views import generic


class AdminHoneypot(generic.FormView):
    template_name = 'admin_honeypot/login.html'
    form_class = HoneypotLoginForm

    def dispatch(self, request, *args, **kwargs):
        if not request.path.endswith('/'):
            return redirect(request.path + '/', permanent=True)
        if django.VERSION >= (1, 7):
            login_url = reverse('admin_honeypot:login')
            if request.path != login_url:
                return redirect('{0}?next={1}'.format(login_url, request.path))
        return super(AdminHoneypot, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class):
        return form_class(self.request, **self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        context = super(AdminHoneypot, self).get_context_data(**kwargs)
        path = self.request.get_full_path()
        context.update({
            'app_path': path,
            REDIRECT_FIELD_NAME: path,
            'title': _('Log in'),
        })
        return context

    def form_valid(self, form):
        return self.form_invalid(form)

    def form_invalid(self, form):
        path = self.request.get_full_path()
        if len(path) > 255:
            path = path[:230] + '...(%d chars)' % len(path)

        instance = LoginAttempt.objects.create(
            username=self.request.POST.get('username'),
            session_key=self.request.session.session_key,
            ip_address=self.request.META.get('REMOTE_ADDR'),
            user_agent=self.request.META.get('HTTP_USER_AGENT'),
            path=path,
        )
        honeypot.send(sender=LoginAttempt, instance=instance, request=self.request)
        return super(AdminHoneypot, self).form_invalid(form)
