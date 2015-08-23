# -*- coding: utf-8 -*-

from django.conf.urls import url
from expedients.views import (
    ExpedientListView, ExpedientCreateView, ExpedientDetailView,
    ExpedientDeleteView, DispatchCreateView
    )

urlpatterns = [
    url(r'^$',
        ExpedientListView.as_view(),
        name='list'
        ),
    url(r'^create/$',
        ExpedientCreateView.as_view(),
        name='create'
        ),

    url(r'^(?P<pk>\d+)/$',
        ExpedientDetailView.as_view(),
        name='detail'
        ),
    url(r'^(?P<pk>\d+)/delete/$',
        ExpedientDeleteView.as_view(),
        name='delete'
        ),
    url(r'^(?P<pk>\d+)/dispatch/$',
        DispatchCreateView.as_view(),
        name='dispatch'
        ),
]
