# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('concourses', '0002_auto_20150807_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 8, 9, 13, 21, 22, 400531, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
