from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm, ERROR_MESSAGE
from django.utils.translation import ugettext as _

class HoneypotLoginForm(AdminAuthenticationForm):
    def clean(self):
        ## Always raise the default error message, because we don't
        ## care what they entered here.
        raise forms.ValidationError(ERROR_MESSAGE)
