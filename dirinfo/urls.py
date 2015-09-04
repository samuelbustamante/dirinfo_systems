# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from concourses import urls as concourses_urls
from events import urls as events_urls
from expedients import urls as expedients_urls
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.contrib import admin

urlpatterns = [
    url(r'^$',
        RedirectView.as_view(url='/accounts/profile/'),
        name='index'
        ),
    url(r'^accounts/login/$',
        auth_views.login,
        name='login'
        ),
    url(r'^accounts/logout/$',
        auth_views.logout_then_login,
        name='logout'
        ),
    url(r'^concourses/',
        include(concourses_urls, namespace='concourses')
        ),
    url(r'^events/',
        include(events_urls, namespace='events')
        ),
    url(r'^expedients/',
        include(expedients_urls, namespace='expedients')
        ),
    url(r'^admin/',
        include(admin.site.urls)
        ),
]
