# -*- coding: utf-8 -*-

from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView
    )
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from events.models import Event


class EventListView(ListView):
    model = Event

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


class EventCreateView(CreateView):
    model = Event
    fields = ['date', 'topic', 'matter', 'description']
    success_url = reverse_lazy('events:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreateView, self).form_valid(form)


class EventUpdateView(UpdateView):
    model = Event
    fields = ['date', 'topic', 'matter', 'description']
    success_url = reverse_lazy('events:list')
    template_name_suffix = '_update_form'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventUpdateView, self).form_valid(form)


class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('events:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventDeleteView, self).dispatch(*args, **kwargs)
