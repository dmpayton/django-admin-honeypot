from django.dispatch import Signal

honeypot = Signal(providing_args=['instance', 'request'])
