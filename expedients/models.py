# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Expedient(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)

    def __str__(self):
        return '{} - {}'.format(self.name, self.number)

    class Meta:
        verbose_name = 'expediente'
        verbose_name_plural = 'expedientes'


class Dispatch(models.Model):
    user = models.ForeignKey(User)
    expedient = models.ForeignKey(Expedient, related_name='dispatchs')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
