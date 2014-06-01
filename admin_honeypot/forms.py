import django
from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm
try:
    from django.contrib.admin.forms import ERROR_MESSAGE
except ImportError:
    ERROR_MESSAGE = AdminAuthenticationForm.error_messages['invalid_login']


class HoneypotLoginForm(AdminAuthenticationForm):
    def clean(self):
        """
        Always raise the default error message, because we don't
        care what they entered here.
        """
        # first check if the form has the username_field attribute
        # set, which indicates custom user model support
        username_field = getattr(self, 'username_field', None)
        if username_field is not None:
            params = {'username': username_field.verbose_name}
            # then raise the validation error in different ways,
            # depending on the Django version
            if django.VERSION >= (1, 6):
                raise forms.ValidationError(ERROR_MESSAGE,
                                            code='invalid',
                                            params=params)
            else:
                raise forms.ValidationError(ERROR_MESSAGE % params)
        # fall back to just using the error message as a string
        raise forms.ValidationError(ERROR_MESSAGE)
