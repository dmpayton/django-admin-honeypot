from admin_honeypot import views
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', views.AdminHoneypot.as_view(), name='login'),
    url(r'^.*$', views.AdminHoneypot.as_view(), name='index'),
]
