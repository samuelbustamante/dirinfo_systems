# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=100)
    code = models.SlugField(max_length=50, unique=True)
    text_color = models.CharField(max_length=20)
    background = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tema'
        verbose_name_plural = 'temas'
        ordering = ['name']


class Event(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    topic = models.ForeignKey(Topic)
    matter = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.matter

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
        ordering = ['date']
