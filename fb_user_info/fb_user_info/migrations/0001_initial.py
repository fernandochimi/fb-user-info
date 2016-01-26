# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token', models.CharField(primary_key=True, default=uuid.uuid4, serialize=False, max_length=128, unique=True, verbose_name='token')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(related_name='token_set', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Token',
            },
        ),
        migrations.CreateModel(
            name='UserFacebookInfo',
            fields=[
                ('facebook_id', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=255, null=True, blank=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('gender', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'User Facebook Info',
                'verbose_name_plural': 'Users Facebook Info',
            },
        ),
    ]
