from django.conf.urls import include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.urls import re_path

admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    re_path(r'^secret/', admin.site.urls),
]
