from django.urls import include, re_path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    re_path(r'^secret/', admin.site.urls),
]
