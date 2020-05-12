import re

from urllib.parse import quote_plus

import django
import pytest

from django.conf import settings
from django.core import mail
from django.test import TestCase
from django.urls import reverse

from admin_honeypot.models import LoginAttempt


class AdminHoneypotTest(TestCase):
    maxDiff = None

    @property
    def admin_login_url(self):
        return reverse('admin:login')

    @property
    def admin_url(self):
        return reverse('admin:index')

    @property
    def honeypot_login_url(self):
        return reverse('admin_honeypot:login')

    @property
    def honeypot_url(self):
        return reverse('admin_honeypot:index')

    def test_same_content(self):
        """
        The honeypot should be an exact replica of the admin login page,
        with the exception of where the form submits to and the CSS to
        hide the user tools.
        """

        admin_html = self.client.get(self.admin_url, follow=True).content.decode('utf-8')
        honeypot_html = (self.client.get(self.honeypot_url, follow=True).content.decode('utf-8')
            # /admin/login/ -> /secret/login/
            .replace(self.honeypot_login_url, self.admin_login_url)

            # "/admin/" -> "/secret/"
            .replace('"{0}"'.format(self.honeypot_url), '"{0}"'.format(self.admin_url))

            # %2fadmin%2f -> %2fsecret%2f
            .replace(quote_plus(self.honeypot_url), quote_plus(self.admin_url))
        )

        # Drop CSRF token
        csrf_re = re.compile(r"(<input [^/>]+ value=['\"])[a-zA-Z0-9]+")
        admin_html = csrf_re.sub(r"\1[']", admin_html)
        honeypot_html = csrf_re.sub(r"\1[']", honeypot_html)

        self.assertEqual(honeypot_html, admin_html)

    def test_create_login_attempt(self):
        """
        A new LoginAttempt object is created
        """
        data = {
            'username': 'admin',
            'password': 'letmein'
        }
        self.client.post(self.honeypot_login_url, data)
        attempt = LoginAttempt.objects.latest('pk')
        self.assertEqual(data['username'], attempt.username)
        self.assertEqual(data['username'], str(attempt))

    def test_email_admins(self):
        """
        An email is sent to settings.ADMINS
        """
        self.client.post(self.honeypot_login_url, {
            'username': 'admin',
            'password': 'letmein'
        })
        # CONSIDER: Is there a better way to do this?
        self.assertTrue(len(mail.outbox) > 0)  # We sent at least one email...
        self.assertIn(settings.ADMINS[0][1], mail.outbox[0].to)  # ...to an admin

    def test_trailing_slash(self):
        """
        /admin redirects to /admin/ permanent redirect.
        """
        url = self.honeypot_url + 'foo/'
        redirect_url = self.honeypot_login_url + '?next=' + url

        response = self.client.get(url.rstrip('/'), follow=True)
        self.assertRedirects(response, redirect_url, status_code=301)

    def test_real_url_leak(self):
        """
        A test to make sure the real admin URL isn't leaked in the honeypot
        login form page.
        """

        honeypot_html = self.client.get(self.honeypot_url, follow=True).content.decode('utf-8')
        self.assertNotIn('{0}'.format(self.admin_url), honeypot_html)
        self.assertNotIn('{0}'.format(self.admin_login_url), honeypot_html)
