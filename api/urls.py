from django.conf.urls import url, include
from rest_framework import routers
from .views import *


urlpatterns = [
    url(r'screens/(?P<pk>[0-9]+)/$', ScreenDetail.as_view()),
    url(r'users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]