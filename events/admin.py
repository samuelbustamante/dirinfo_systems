# -*- coding: utf-8 -*-

from django.contrib import admin
from events.models import Topic, Event


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
