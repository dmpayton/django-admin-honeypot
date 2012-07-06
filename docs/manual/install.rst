Installation
============

Requirements
------------

* Django 1.3+ (but may work with prior versions)

Install
-------

django-admin-honeypot is on `PyPI`_ and can be installed with `pip`_:

::

    pip install django-admin-honeypot

.. _PyPI: http://pypi.python.org/
.. _pip: http://www.pip-installer.org/

Setup
-----

1. Add ``admin_honeypot`` to ``INSTALLED_APPS`` in settings.py:

::

    INSTALLED_APPS = (
        ...
        'admin_honeypot',
        ...
    )

2. Update urls.py:

::

    urlpatterns = patterns(''
        ...
        url(r'^admin/', include('admin_honeypot.urls')),
        url(r'^secret/', include(admin.site.urls)),
        ...
    )
