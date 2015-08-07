# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concourses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professorresult',
            name='result',
            field=models.ForeignKey(to='concourses.Result', related_name='professors_result'),
        ),
    ]
