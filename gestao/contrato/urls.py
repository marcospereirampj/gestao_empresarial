# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from gestao.contrato.views.despesas_contrato import despesas_contrato
from gestao.contrato.views.documentos_contrato import documentos_contrato
from gestao.contrato.views.editar_despesa_contrato import \
    editar_despesa_contrato
from gestao.contrato.views.editar_documento_contrato import \
    editar_documento_contrato
from gestao.contrato.views.editar_faturamento_contrato import \
    editar_faturamento_contrato
from gestao.contrato.views.equipe_contrato import equipe_contrato
from gestao.contrato.views.faturamentos_contrato import faturamentos_contrato
from gestao.contrato.views.remove_despesa_contrato import \
    remove_despesa_contrato
from gestao.contrato.views.remove_documento_contrato import \
    remove_documento_contrato
from gestao.contrato.views.remove_faturamento_contrato import \
    remove_faturamento_contrato
from gestao.contrato.views.remove_funcionario_equipe import \
    remove_funcionario_equipe
from gestao.contrato.views.detalhes_contrato import detalhes_contrato

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^editar_faturamento_contrato/(?P<id_contrato>\d+)/$', 
            admin.site.admin_view(editar_faturamento_contrato),
            name="editar_faturamento_contrato"),                                           
    url(r'^editar_faturamento_contrato/(?P<id_contrato>\d+)/(?P<id_faturamento_contrato>\d+)/$', 
            admin.site.admin_view(editar_faturamento_contrato),
            name="editar_faturamento_contrato"),                  
    url(r'^faturamentos_contrato/(?P<id_contrato>\d+)/$', 
            admin.site.admin_view(faturamentos_contrato),
            name="faturamentos_contrato"),
    url(r'^remove_faturamento_contrato/(?P<id_faturamento_contrato>\d+)/$', 
            admin.site.admin_view(remove_faturamento_contrato),
            name="remove_faturamento_contrato"),
                       
    url(r'^editar_despesa_contrato/(?P<id_contrato>\d+)/$', 
            admin.site.admin_view(editar_despesa_contrato),
            name="editar_despesa_contrato"),                       
    url(r'^editar_despesa_contrato/(?P<id_contrato>\d+)/(?P<id_despesa_contrato>\d+)/$', 
            admin.site.admin_view(editar_despesa_contrato),
            name="editar_despesa_contrato"),
    url(r'^despesas_contrato/(?P<id_contrato>\d+)/$', 
            admin.site.admin_view(despesas_contrato),
            name="despesas_contrato"),
    url(r'^remove_despesa_contrato/(?P<id_despesa_contrato>\d+)/$', 
            admin.site.admin_view(remove_despesa_contrato),
            name="remove_despesa_contrato"),

    url(r'^equipe_contrato/(?P<id_contrato>\d+)/$', 
            admin.site.admin_view(equipe_contrato),
            name="equipe_contrato"),                       
    url(r'^remove_funcionario_equipe/(?P<id_funcionario>\d+)/$', 
            admin.site.admin_view(remove_funcionario_equipe),
            name="remove_funcionario_equipe"),

    url(r'^editar_documento_contrato/(?P<id_contrato>\d+)/$', 
            admin.site.admin_view(editar_documento_contrato),
            name="editar_documento_contrato"),                       
    url(r'^editar_documento_contrato/(?P<id_contrato>\d+)/(?P<id_documento_contrato>\d+)/$', 
            admin.site.admin_view(editar_documento_contrato),
            name="editar_documento_contrato"),
    url(r'^documentos_contrato/(?P<id_contrato>\d+)/$', 
            admin.site.admin_view(documentos_contrato),
            name="documentos_contrato"),
    url(r'^remove_documento_contrato/(?P<id_documento_contrato>\d+)/$', 
           admin.site.admin_view(remove_documento_contrato),
           name="remove_documento_contrato"),

    url(r'^detalhes_contrato/(?P<id_contrato>\d+)/$', 
           admin.site.admin_view(detalhes_contrato),
           name="detalhes_contrato"),

    (r'^/', include(admin.site.urls)),
)