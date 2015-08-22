# -*- coding: utf-8 -*-

from django.conf.urls import url
from expedients.views import (
    ExpedientDetailView, ExpedientListView, ExpedientCreateView
    )

urlpatterns = [
    url(r"^$",
        ExpedientListView.as_view(),
        name="list"
        ),
    url(r'^(?P<pk>\d+)/$',
        ExpedientDetailView.as_view(),
        name='detail'
        ),
    url(r"^create/$",
        ExpedientCreateView.as_view(),
        name="create"
        ),
]
