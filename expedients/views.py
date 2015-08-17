# -*- coding: utf-8 -*-

from django.views.generic import CreateView, ListView
from expedients.models import Expedient, Dispatch


class ExpedientListView(ListView):
    model = Expedient

    def get_queryset(self):
        # Los expedientes donde el último despacho
        # tenga como user a request.user
        return self.model.objects.filter(
            dispatchs__user=self.request.user,
            dispatchs__in=Dispatch.objects.all().distinct('expedient')
            ).order_by('dispatchs')


class ExpedientCreateView(CreateView):
    model = Expedient
    fields = ['name', 'number']
