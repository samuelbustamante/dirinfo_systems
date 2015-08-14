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
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('matter', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['date'],
                'verbose_name_plural': 'eventos',
                'verbose_name': 'evento',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.SlugField(unique=True)),
                ('text_color', models.CharField(max_length=20)),
                ('background', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'temas',
                'verbose_name': 'tema',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='topic',
            field=models.ForeignKey(to='events.Topic'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
