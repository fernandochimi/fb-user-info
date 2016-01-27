# coding utf-8
import uuid

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Token(models.Model):
    user = models.ForeignKey(
        User, related_name='token_set', null=True, blank=True)
    token = models.CharField(
        u'token', max_length=128, unique=True,
        default=uuid.uuid4, primary_key=True)
    date_added = models.DateTimeField(
        default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}'.format(self.token)

    class Meta:
        verbose_name, verbose_name_plural = "Token", "Token"


class UserFacebookInfo(models.Model):
    facebook_id = models.IntegerField(primary_key=True)
    link = models.URLField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return u'{0}'.format(self.facebook_id)

    class Meta:
        verbose_name, verbose_name_plural = (
            "User Facebook Info", "Users Facebook Info")
