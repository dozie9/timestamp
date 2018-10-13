from django.conf.urls import url
from timestamp import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
]