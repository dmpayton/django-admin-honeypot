import django
import pytest
from admin_honeypot.models import LoginAttempt
from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase


class AdminHoneypotTest(TestCase):
    maxDiff = None

    @property
    def admin_url(self):
        if django.VERSION >= (1, 7):
            return reverse('admin:login')
        return reverse('admin:index')

    @property
    def honeypot_url(self):
        if django.VERSION >= (1, 7):
            return reverse('admin_honeypot:login')
        return reverse('admin_honeypot:index')

    def test_same_content(self):
        """
        The honeypot should be an exact replica of the admin login page,
        with the exception of where the form submits to and the CSS to
        hide the user tools.
        """

        admin_html = self.client.get(self.admin_url, follow=True).content.decode('utf-8')
        honeypot_html = self.client.get(self.honeypot_url, follow=True).content.decode('utf-8').replace(
            '"{0}"'.format(self.honeypot_url),
            '"{0}"'.format(self.admin_url)
        )

        self.assertEqual(honeypot_html, admin_html)

    def test_create_login_attempt(self):
        """
        A new LoginAttempt object is created
        """
        data = {
            'username': 'admin',
            'password': 'letmein'
        }
        self.client.post(self.honeypot_url, data)
        attempt = LoginAttempt.objects.latest('pk')
        self.assertEqual(data['username'], attempt.username)
        self.assertEqual(data['username'], str(attempt))

    def test_email_admins(self):
        """
        An email is sent to settings.ADMINS
        """
        self.client.post(self.honeypot_url, {
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
        redirect_url = url = reverse('admin_honeypot:index') + 'foo/'

        # Django 1.7 will redirect the user, but the ?next param will
        # have the trailing slash.
        if django.VERSION >= (1, 7):
            redirect_url = reverse('admin_honeypot:login') + '?next=' + url

        response = self.client.get(url.rstrip('/'), follow=True)
        self.assertRedirects(response, redirect_url, status_code=301)

    @pytest.mark.skipif(django.VERSION >= (1, 7), reason="POST requests won't work with Django 1.7's admin redirect strategy")
    def test_arbitrary_urls(self):
        """
        The Django admin displays a login screen for everything under /admin/
        """
        data = {
            'username': 'admin',
            'password': 'letmein',
        }
        url_list = (
            'auth/',
            'comments/moderate/',
            'flatpages/flatpage/?ot=desc&o=1'
            'auth/user/1/',
        )
        base_url = self.honeypot_url
        for url in url_list:
            self.client.post(base_url + url, data)
            attempt = LoginAttempt.objects.latest('pk')
            self.assertEqual(base_url + url, attempt.path)
            self.assertEqual(data['username'], attempt.username)
