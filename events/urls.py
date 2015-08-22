# -*- coding: utf-8 -*-

from django.conf.urls import url
from events.views import (
    EventListView, EventCreateView, EventUpdateView, EventDeleteView
    )

urlpatterns = [
    url(r'^$',
        EventListView.as_view(),
        name='list'
        ),
    url(r'^create/$',
        EventCreateView.as_view(),
        name='create'
        ),
    url(r'^(?P<pk>\d+)/update/$',
        EventUpdateView.as_view(),
        name='update'
        ),
    url(r'^(?P<pk>\d+)/delete/$',
        EventDeleteView.as_view(),
        name='delete'
        ),
]
