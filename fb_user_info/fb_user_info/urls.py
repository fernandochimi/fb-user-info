# coding: utf-8
from django.conf.urls import url, patterns, include

from resources import UserFacebookInfoResource


urlpatterns = patterns(
    '',
    url(r'^api/v1/fb-user/', include(UserFacebookInfoResource.urls())),
)
