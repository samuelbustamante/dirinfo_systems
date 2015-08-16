# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('received', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Expedient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'expedientes',
                'verbose_name': 'expediente',
            },
        ),
        migrations.AddField(
            model_name='dispatch',
            name='expedient',
            field=models.ForeignKey(to='expedients.Expedient', related_name='dispatchs'),
        ),
        migrations.AddField(
            model_name='dispatch',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
