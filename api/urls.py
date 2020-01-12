from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url('snips/', views.api_snip),
    url('^snip/(?P<id>\d+)$', views.list_snip),
]

