#-*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
import gestao.basico.views.index

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', admin.site.admin_view( gestao.basico.views.index.index )),
    url(r'', include(admin.site.urls)),
    (r'^recursos_humanos/', include ('gestao.recursos_humanos.urls')),
    (r'^financeiro/', include ('gestao.financeiro.urls')),
    (r'^contrato/', include ('gestao.contrato.urls')),
    (r'^relatorio/', include ('gestao.relatorio.urls')),
    (r'^administracao_geral/', include ('gestao.administracao_geral.urls')),
)
