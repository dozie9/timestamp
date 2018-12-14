from django.conf.urls import url
from timestamp import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^timestamp/(?P<date>[-0-9]+)/$', views.timestamp, name="timestamp"),
    url(r'^timestamp/(?P<error>[\D\d]+)/$', views.invalid_date, name="invalid_date"),
    url(r'^api/whoami/$', views.whoami, name="whoami"),
]
