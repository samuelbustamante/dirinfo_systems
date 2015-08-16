# -*- coding: utf-8 -*-

from django.contrib import admin
from expedients.models import Expedient, Dispatch


class DispatchInline(admin.TabularInline):
    model = Dispatch


@admin.register(Expedient)
class ExpedientAdmin(admin.ModelAdmin):
    inlines = [DispatchInline]
