# -*- coding: utf-8 -*-

from django.views.generic import CreateView, ListView, DeleteView
from django.core.urlresolvers import reverse_lazy
from events.models import Event


class EventListView(ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


class EventCreateView(CreateView):
    model = Event
    fields = ['date', 'topic', 'matter', 'description']
    success_url = reverse_lazy('events:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreateView, self).form_valid(form)


class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('events:list')
