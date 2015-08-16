# -*- coding: utf-8 -*-

from django.conf.urls import url
from expedients.views import ExpedientListView, ExpedientCreateView

urlpatterns = [
    url(r"^$",
        ExpedientListView.as_view(),
        name="list"
        ),
    url(r"^create/$",
        ExpedientCreateView.as_view(),
        name="create"
        ),
]
