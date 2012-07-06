#!/usr/bin/env python
"""
django-admin-honeypot
=====================

A fake Django admin login screen to notify admins of attempted unauthorized
access. This app was inspired by discussion in and around Paul McMillan's
security talk at DjangoCon 2011.

Basic Usage:

* Add ``admin_honeypot`` to ``settings.INSTALLED_APPS``
* Update urls.py::

    urlpatterns = patterns(''
        ...
        url(r'^admin/', include('admin_honeypot.urls')),
        url(r'^secret/', include(admin.site.urls)),
    )
"""
import os
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
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    keywords='django admin honeypot trap',
    maintainer = 'Derek Payton',
    maintainer_email = 'derek.payton@gmail.com',
    url='https://github.com/dmpayton/django-admin-honeypot',
    download_url='https://github.com/dmpayton/django-admin-honeypot/tarball/v%s' % __version__,
    license=__license__,
    include_package_data=True,
    packages=find_packages(exclude=('tests',)),
    test_suite='tests.setuptest.SetupTestSuite',
    tests_require=(
        'coverage',
        'django',
        'pep8==1.3.1',
      ),
    zip_safe=False,
    )
