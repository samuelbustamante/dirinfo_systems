# -*- coding: utf-8 -*-

from django.views.generic import CreateView, ListView, DetailView
from expedients.models import Expedient, Dispatch
from django.core.urlresolvers import reverse


class ExpedientCreateView(CreateView):
    model = Expedient
    fields = ['name', 'number']

    def get_success_url(self):
        return reverse('expedients:detail', kwargs={'pk': self.object.pk})


class ExpedientListView(ListView):
    model = Expedient

    def get_queryset(self):
        # Los expedientes donde el último despacho
        # tenga como user a request.user
        return self.model.objects.filter(
            dispatchs__user=self.request.user,
            dispatchs__in=Dispatch.objects.all().distinct('expedient')
            ).order_by('dispatchs')


class ExpedientDetailView(DetailView):
    model = Expedient
