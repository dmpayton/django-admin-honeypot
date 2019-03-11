import os
from admin_honeypot.signals import honeypot
from admin_honeypot.hpf import hpflogger
from django.conf import settings
from django.core.mail import mail_admins
from django.template.loader import render_to_string
from django.urls import reverse


hpfl = False
if getattr(settings, 'ADMIN_HONEYPOT_REPORT_HPFEEDS', False):
    environreq = [
        'HPFEEDS_SERVER',
        'HPFEEDS_PORT',
        'HPFEEDS_IDENT',
        'HPFEEDS_SECRET',
        'HPFEEDS_CHANNEL',
        'SERVERID',
        ]
    if all(var in os.environ for var in environreq):
        hpf_server = os.environ.get('HPFEEDS_SERVER', False)
        hpf_port = int(os.environ.get('HPFEEDS_PORT'))
        hpf_ident = os.environ.get('HPFEEDS_IDENT')
        hpf_secret = os.environ.get('HPFEEDS_SECRET')
        hpf_channel = os.environ.get('HPFEEDS_CHANNEL')
        hpf_serverid = os.environ.get('HPFEEDS_SERVERID')
    else:
        hpf_server = getattr(settings, 'HPFEEDS_SERVER', False)
        hpf_port = getattr(settings, 'HPFEEDS_PORT')
        hpf_ident = getattr(settings, 'HPFEEDS_IDENT')
        hpf_secret = getattr(settings, 'HPFEEDS_SECRET')
        hpf_channel = getattr(settings, 'HPFEEDS_CHANNEL')
        hpf_serverid = getattr(settings, 'HPFEEDS_SERVERID')

    if hpf_server:
        hpfl = hpflogger(hpf_server, hpf_port, hpf_ident, hpf_secret, hpf_channel, hpf_serverid)

def notify_admins(instance, request, **kwargs):
    path = reverse('admin:admin_honeypot_loginattempt_change', args=(instance.pk,))
    admin_detail_url = 'http://{0}{1}'.format(request.get_host(), path)
    context = {
        'request': request,
        'instance': instance,
        'admin_detail_url': admin_detail_url,
    }
    subject = render_to_string('admin_honeypot/email_subject.txt', context).strip()
    message = render_to_string('admin_honeypot/email_message.txt', context).strip()
    mail_admins(subject=subject, message=message)

def report_hpfeeds(instance, request, **kwargs):
    if getattr(settings, 'ADMIN_HONEYPOT_RECORD_PASSWORD', False):
        password_to_store = self.request.POST.get('password')
    else:
        password_to_store = None
    msg = {
        'timestamp:': instance.timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'src_ip': request.META.get('REMOTE_ADDR'),
        'src_port': request.META.get('SERVER_PORT'),
        'user_agent': request.META.get('HTTP_USER_AGENT'),
        'path': request.get_full_path(),
        'uri': request.build_absolute_uri(),
        'body': request.body.decode('utf-8', 'ignore'),
        'method': request.method,
        'scheme': request.scheme,
        'content_type': request.content_type,
        'encoding': request.encoding,
        'username': request.POST.get('username'),
        'password': password_to_store
    }
    hpfl.log(msg)

if getattr(settings, 'ADMIN_HONEYPOT_EMAIL_ADMINS', True):
    honeypot.connect(notify_admins)

if hpfl:
    conn = honeypot.connect(report_hpfeeds)