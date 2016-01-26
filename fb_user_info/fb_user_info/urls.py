# coding: utf-8
from django.conf.urls import url, patterns, include

from resources import UserFacebookInfo


urlpatterns = patterns(
    '',
    url(r'^api/v1/fb-user/', include(UserFacebookInfo.urls())),
)
