# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Professor(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    area = models.ForeignKey(Area, related_name='professors')
    #elected = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.area)


class Result(models.Model):
    title = models.CharField(max_length=100)
    area = models.ForeignKey(Area, related_name='results')

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class ProfessorResult(models.Model):
    professor = models.ForeignKey(Professor)
    result = models.ForeignKey(Result, related_name='professors')
