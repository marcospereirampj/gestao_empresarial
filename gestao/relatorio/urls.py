# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns, include
from django.contrib import admin
from gestao.relatorio.views.contratos_ativos import contratos_ativos

admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^contratos_ativos/$',
    admin.site.admin_view(contratos_ativos),
    name='contratos_ativos'),
                                              
    (r'^/', include(admin.site.urls)),
)
