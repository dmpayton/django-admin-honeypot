#!/usr/bin/env python
"""
django-admin-honeypot
=====================

A fake Django admin login screen to notify admins of attempted unauthorized
access. This app was inspired by discussion in and around Paul McMillan's
security talk at DjangoCon 2011.

|travis-ci|_ |coverage-io|_ |downloads|_

.. |travis-ci| image:: https://secure.travis-ci.org/dmpayton/django-admin-honeypot.png
.. _travis-ci: https://travis-ci.org/dmpayton/django-admin-honeypot

.. |coverage-io| image:: https://coveralls.io/repos/dmpayton/django-admin-honeypot/badge.png
.. _coverage-io: https://coveralls.io/r/dmpayton/django-admin-honeypot

.. |downloads| image:: https://pypip.in/d/django-admin-honeypot/badge.png
.. _downloads: https://pypi.python.org/pypi/django-admin-honeypot


Basic Usage:

* Add ``admin_honeypot`` to ``settings.INSTALLED_APPS``
* Update urls.py::

    urlpatterns = patterns(''
        ...
        url(r'^admin/', include('admin_honeypot.urls')),
        url(r'^secret/', include(admin.site.urls)),
    )
"""

import sys
from admin_honeypot import __version__, __description__, __license__

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='django-admin-honeypot',
    version=__version__,
    description=__description__,
    long_description=__doc__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    keywords='django admin honeypot trap',
    maintainer='Derek Payton',
    maintainer_email='derek.payton@gmail.com',
    url='https://github.com/dmpayton/django-admin-honeypot',
    download_url='https://github.com/dmpayton/django-admin-honeypot/tarball/v%s' % __version__,
    license=__license__,
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    )
