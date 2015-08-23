# -*- coding: utf-8 -*-

from django.conf.urls import url
from concourses.views import (
    ResultListView, ResultCreateView, ResultDeleteView
    )

urlpatterns = [
    url(r'^$',
        ResultListView.as_view(),
        name='list'
        ),
    url(r'^create/$',
        ResultCreateView.as_view(),
        name='create'
        ),
    url(r'^(?P<pk>\d+)/delete/$',
        ResultDeleteView.as_view(),
        name='delete'
        ),
]
