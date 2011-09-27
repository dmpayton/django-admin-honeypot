from admin_honeypot.models import LoginAttempt
from django.core.urlresolvers import reverse
from django.test import TestCase


class AdminHoneypotTest(TestCase):
    urls = 'admin_honeypot.urls'

    def test_admin_honeypot(self):
        data = {
            'username': 'admin',
            'password': 'letmein'
            }
        response = self.client.post(reverse('admin_honeypot'), data)
        attempt = LoginAttempt.objects.latest('pk')
        self.assertEqual(data['username'], attempt.username)
        self.assertEqual(data['password'], attempt.password)

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
