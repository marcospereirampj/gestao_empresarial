# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('', 
    (r'^/', include(admin.site.urls)),
)