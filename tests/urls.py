import django
from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

if django.VERSION < (2, 0):
    urlpatterns = [
        url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
        url(r'^secret/', include(admin.site.urls)),
    ]
else:
    from django.urls import path
    urlpatterns = [
        path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
        path('secret/', admin.site.urls),
    ]
