from admin_honeypot.models import LoginAttempt
from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase
#from django.test.utils import override_settings # Waiting on 1.4

class AdminHoneypotTest(TestCase):
    urls = 'admin_honeypot.urls'

    def test_create_login_attempt(self):
        """
        A new LoginAttempt object is created
        """
        data = {
            'username': 'admin',
            'password': 'letmein'
            }
        response = self.client.post(reverse('admin_honeypot'), data)
        attempt = LoginAttempt.objects.latest('pk')
        self.assertEqual(data['username'], attempt.username)
        self.assertEqual(data['password'], attempt.password)

    #@override_settings(ADMINS=(('Admin User', 'admin@example.com'),))
    def test_email_admins(self):
        """
        An email is sent to settings.ADMINS
        """
        response = self.client.post(reverse('admin_honeypot'), {
            'username': 'admin',
            'password': 'letmein'
            })
        ## CONSIDER: Is there a better way to do this?
        self.assertTrue(len(mail.outbox) > 0) ## We sent at least one email...
        self.assertIn(settings.ADMINS[0][1], mail.outbox[0].to) ## ...to someone listed as an admin

    def test_arbitrary_urls(self):
        """
        The Django admin displays a login screen for everything under /admin/
        """
        data = {
            'username': 'admin',
            'password': 'letmein',
        }
        base_url = reverse('admin_honeypot')
        for url in ('auth/', 'comments/moderate/', 'auth/user/1/'):
            response = self.client.post(base_url + url, data)
            attempt = LoginAttempt.objects.latest('pk')
            self.assertEqual(data['username'], attempt.username)
            self.assertEqual(data['password'], attempt.password)

    def test_trailing_slash(self):
        """
        /admin/foo redirects to /admin/foo/ permanent redirect.
        """
        url = reverse('admin_honeypot')
        response = self.client.get(url + 'foo')
        self.assertRedirects(response, url + 'foo/', status_code=301)
