=====================
django-admin-honeypot
=====================

|travis-ci|_ |coverage-io|_ |downloads|_

.. |travis-ci| image:: https://secure.travis-ci.org/dmpayton/django-admin-honeypot.png?branch=develop
.. _travis-ci: https://travis-ci.org/dmpayton/django-admin-honeypot

.. |coverage-io| image:: https://coveralls.io/repos/dmpayton/django-admin-honeypot/badge.png?branch=develop
.. _coverage-io: https://coveralls.io/r/dmpayton/django-admin-honeypot

.. |downloads| image:: https://pypip.in/d/django-admin-honeypot/badge.png
.. _downloads: https://pypi.python.org/pypi/django-admin-honeypot

**django-admin-honeypot** is a fake Django admin login screen to log and notify
admins of attempted unauthorized access. This app was inspired by discussion
in and around Paul McMillan's security talk at DjangoCon 2011.

* **Author**: `Derek Payton <http://dmpayton.com/>`_
* **Version**: 0.4.0
* **License**: MIT

Documentation
=============

http://django-admin-honeypot.readthedocs.org

tl;dr
-----

* Install django-admin-honeypot from PyPI::

        pip install django-admin-honeypot

* Add ``admin_honeypot`` to ``INSTALLED_APPS``
* Update your urls.py:

    *New in v0.4: The* ``namespace`` *argument is now required.*

    ::

        urlpatterns = patterns(''
            ...
            url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
            url(r'^secret/', include(admin.site.urls)),
        )

* Run ``python manage.py syncdb`` or with south ``python manage.py migrate``
