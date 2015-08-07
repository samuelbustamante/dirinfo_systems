# -*- coding: utf-8 -*-

from django.contrib import admin
from concourses.models import Area, Professor, Result, ProfessorResult


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass


class ProfessorResultInline(admin.TabularInline):
    model = ProfessorResult


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    inlines = [ProfessorResultInline]
