#!/usr/bin/env python

import os
from admin_honeypot import __version__, __description__, __license__
from setuptools import setup, find_packages

## Package detection from django-registration

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('admin_honeypot'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[11:] # Strip "admin_honeypot/" or "admin_honeypot\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(
    name='django-admin-honeypot',
    version=__version__,
    description=__description__,
    long_description=open(os.path.join(root_dir, 'README.mkd')).read(),
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
    packages=packages,
    package_data={'admin_honeypot': data_files},
    package_dir={'admin_honeypot': 'admin_honeypot'},
    zip_safe=False,
    )
