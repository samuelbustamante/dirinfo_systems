# -*- coding: utf-8 -*-

from django.views.generic import (
    ListView, CreateView, DetailView, DeleteView
    )
from django.core.urlresolvers import reverse, reverse_lazy
from expedients.models import Expedient, Dispatch


class ExpedientListView(ListView):
    model = Expedient

    def get_queryset(self):
        if self.request.user.username == 'sabustamante':
            return Expedient.objects.all()
        else:
            # Los expedientes donde el último despacho
            # tenga como user a request.user
            return self.model.objects.filter(
                dispatchs__user=self.request.user,
                dispatchs__in=Dispatch.objects.all().distinct('expedient')
                ).order_by('dispatchs')


class ExpedientCreateView(CreateView):
    model = Expedient
    fields = ['name', 'number']

    def get_success_url(self):
        return reverse('expedients:dispatch', kwargs={'pk': self.object.pk})


class ExpedientDetailView(DetailView):
    model = Expedient


class ExpedientDeleteView(DeleteView):
    model = Expedient
    success_url = reverse_lazy('expedients:list')


class DispatchCreateView(CreateView):
    model = Dispatch
    fields = ['user']
    success_url = reverse_lazy('expedients:list')

    def get_context_data(self, **kwargs):
        context = super(DispatchCreateView, self).get_context_data(**kwargs)
        context['object'] = Expedient.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        expedient = Expedient.objects.get(pk=self.kwargs.get('pk'))
        form.instance.expedient = expedient
        return super(DispatchCreateView, self).form_valid(form)
