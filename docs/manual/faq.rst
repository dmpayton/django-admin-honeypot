==========================
Frequently Asked Questions
==========================

Why can't I delete login attempts from the Django admin?
========================================================

The delete permission has been set to false for all users -- including
superusers -- as an added security precaution. This is done so that, in the
event that an attacker does make it into your admin, it will be harder to cover
up their tracks if they had previously tried to break in through the honeypot.

Why is the IP address logged as 127.0.0.1?
==========================================

Django-admin-honeypot pulls the users IP address from the ``REMOTE_ADDR``
request header. If your Django app is behind a load balancer or proxy web
server, this may not be set and instead you will have an ``HTTP_X_FORWARDED_FOR``
header which contains the IP address in a comma-separated string.

The simple solution is to use a middleware to automatically set ``REMOTE_ADDR``
to the value of ``HTTP_X_FORWARDED_FOR``, like so:

::

    class RemoteAddrMiddleware(object):
        def process_request(self, request):
            if 'HTTP_X_FORWARDED_FOR' in request.META:
                ip = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0].strip()
                request.META['REMOTE_ADDR'] = ip

See also: http://docs.webfaction.com/software/django/troubleshooting.html#accessing-remote-addr
