# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from concourses import urls as concourses_urls
from events import urls as events_urls
from django.contrib import admin

urlpatterns = [
    url(r'^concourses/', include(concourses_urls, namespace='concourses')),
    url(r'^events/', include(events_urls, namespace='events')),
    url(r'^admin/', include(admin.site.urls)),
]
