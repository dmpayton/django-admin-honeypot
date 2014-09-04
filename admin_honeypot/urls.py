import django
from admin_honeypot import views

try:
    from django.conf.urls import patterns, include, url
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('')

# Add /admin/login/ for Django 1.7+
if django.VERSION >= (1, 7):
    urlpatterns += patterns('',
        url(r'^login/$', views.AdminHoneypot.as_view(), name='login'),
    )

urlpatterns += patterns('',
    url(r'^.*$', views.AdminHoneypot.as_view(), name='index'),
)
