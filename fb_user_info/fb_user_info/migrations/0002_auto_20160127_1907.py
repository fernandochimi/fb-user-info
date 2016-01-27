# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb_user_info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfacebookinfo',
            name='username',
        ),
        migrations.AddField(
            model_name='userfacebookinfo',
            name='link',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
    ]
