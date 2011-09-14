from admin_honeypot.models import LoginAttempt
from django.core.urlresolvers import reverse
from django.test import TestCase


class AdminHoneypotTest(TestCase):
    def test_admin_honeypot(self):
        data = {
            'username': 'admin',
            'password': 'letmein'
            }
        response = self.client.post(reverse('admin_honeypot'), data)
        attempt = LoginAttempt.objects.latest('pk')
        self.assertEqual(data['username'], data['username'])
        self.assertEqual(data['password'], data['password'])
