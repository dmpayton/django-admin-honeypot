=====
Usage
=====

Basic setup
===========

1. Add ``admin_honeypot`` to ``INSTALLED_APPS`` in settings.py::

    INSTALLED_APPS = (
        ...
        'admin_honeypot',
        ...
    )

2. Update urls.py::

    urlpatterns = [
        ...
        path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
        path('secret/', admin.site.urls),
    ]

3. Run migration::

   $ python manage.py migrate

The ``honeypot`` signal
=======================

Every time a login attempt occurs, the :func:`admin_honeypot.signals.honeypot`
signal is fired off. You can setup listeners to this in order to send out any
custom notifications or logging.

A default listener, :func:`admin_honeypot.listeners.notify_admins`, will send
an email to all site administrators (``ADMINS`` in your site settings) with the
details. This can be disabled by setting ``ADMIN_HONEYPOT_EMAIL_ADMINS`` to
false in your site settings.

Customizing the login template
==============================

The template rendered on the honeypot is ``admin_honeypot/login.html``. By
default this template simply extends ``admin/login.html``, but you may want
to change it if, e.g.,  you've customized the Django admin and want to display
the stock admin login form.
