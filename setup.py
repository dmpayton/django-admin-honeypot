#!/usr/bin/env python
from setuptools import setup, find_packages

from admin_honeypot import __version__, __description__, __license__

with open('README.rst') as f:
    long_description = f.read()


setup(
    name='django-admin-honeypot-updated-2021',
    version=__version__,
    description=__description__,
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='django admin honeypot trap',
    author='Derek Payton',
    author_email='derek.payton@gmail.com',
    maintainer='blag',
    maintainer_email='blag@users.noreply.github.com',
    url='https://github.com/blag/django-admin-honeypot',
    download_url=f'https://github.com/blag/django-admin-honeypot/tarball/v{__version__}',
    license=__license__,
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=[
        'django>=2.2',
        'django-ipware',
    ],
    extras_require={
        'tests': [
            'pytest',
            'pytest-cov',
            'pytest-django',
            'pytest-flake8',
            'pytest-pythonpath',
        ],
    },
)
