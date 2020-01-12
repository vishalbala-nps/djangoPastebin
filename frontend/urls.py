from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^view/(?P<id>\d+)$', views.viewsnip),
    url('', views.home),
]