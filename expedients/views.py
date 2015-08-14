# -*- coding: utf-8 -*-

from django.views.generic import CreateView, ListView
from expedients.models import Expedient, Dispatch


class ExpedientListView(ListView):
    model = Expedient

    def get_queryset(self):
        # Los expedientes donde el último dispatch
        # tenga como user a request.user



class ExpedientCreateView(CreateView):
    model = Expedient
    fields = ['name', 'number']
