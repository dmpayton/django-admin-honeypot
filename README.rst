=====================
django-admin-honeypot
=====================

.. image:: https://travis-ci.org/dmpayton/django-admin-honeypot.svg?branch=develop
   :target: https://travis-ci.org/dmpayton/django-admin-honeypot
   :alt: Travis-CI

.. image:: https://coveralls.io/repos/dmpayton/django-admin-honeypot/badge.svg?branch=develop
   :target: https://coveralls.io/r/dmpayton/django-admin-honeypot
   :alt: Coverage

.. image:: https://codeclimate.com/github/dmpayton/django-admin-honeypot/badges/gpa.svg?branch=develop
   :target: https://codeclimate.com/github/dmpayton/django-admin-honeypot
   :alt: Code Climate


**django-admin-honeypot** is a fake Django admin login screen to log and notify
admins of attempted unauthorized access. This app was inspired by discussion
in and around Paul McMillan's security talk at DjangoCon 2011.

* **Author**: `Derek Payton <http://dmpayton.com/>`_
* **Version**: 1.1.0
* **License**: MIT

Documentation
=============

http://django-admin-honeypot.readthedocs.io

tl;dr
-----

* Install django-admin-honeypot from PyPI::

        pip install django-admin-honeypot

* Add ``admin_honeypot`` to ``INSTALLED_APPS``
* Update your urls.py:

    ::

        urlpatterns = [
            ...
            path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
            path('secret/', admin.site.urls),
        ]

* Run ``python manage.py migrate``

NOTE: replace ``secret`` in the url above with your own secret url prefix
