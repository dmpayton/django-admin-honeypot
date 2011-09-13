from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm, ERROR_MESSAGE
from django.utils.translation import ugettext as _

class HoneypotLoginForm(AdminAuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        message = ERROR_MESSAGE
        if '@' in username:
            message = _("Your e-mail address is not your username. Try '%s' instead.") % user.username
        raise forms.ValidationError(message)
