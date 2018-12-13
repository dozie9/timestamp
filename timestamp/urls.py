from django.conf.urls import url
from timestamp import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^timestamp/(?P<date>[-0-9]+)/$', views.timestamp, name="timestamp"),
    url(r'^timestamp/(?P<unix_time>[0-9]+)/$', views.unix_timestamp, name="unix_timestamp"),
    url(r'^api/whoami/$', views.whoami, name="whoami"),
]
