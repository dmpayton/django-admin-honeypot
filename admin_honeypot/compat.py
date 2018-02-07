"""
Compatibility layer for various django and python versions imports
"""

try:
    from django.urls import reverse
except ImportError:  # For Django version less than 2.0
    from django.core.urlresolvers import reverse  # noqa

try:
    # Python 2.7
    from urllib import quote_plus
except ImportError:
    # Python 3+
    from urllib.parse import quote_plus  # noqa
