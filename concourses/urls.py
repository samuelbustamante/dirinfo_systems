# -*- coding: utf-8 -*-

from django.conf.urls import url
from concourses.views import *

urlpatterns = [
    url(r'^$',
        ResultListView.as_view(),
        name='result_list'
        ),
    url(r'^(?P<pk>\d+)/$',
        ResultDetailView.as_view(),
        name='result_detail'
        ),
    url(r'^create/$',
        ResultCreateView.as_view(),
        name='result_create'
        ),
]
