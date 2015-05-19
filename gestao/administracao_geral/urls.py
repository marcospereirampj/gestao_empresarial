# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from gestao.administracao_geral.views.detalhes_reuniao import detalhes_reuniao
from gestao.administracao_geral.views.editar_item_ata import editar_item_ata
from gestao.administracao_geral.views.editar_participante_externo import \
    editar_participante_externo
from gestao.administracao_geral.views.editar_participante_interno import \
    editar_participante_interno
from gestao.administracao_geral.views.editar_reuniao import editar_reuniao
from gestao.administracao_geral.views.relatorio_reuniao import relatorio_reuniao
from gestao.administracao_geral.views.remove_item_ata import remove_item_ata
from gestao.administracao_geral.views.remove_participante_externo import \
    remove_participante_externo
from gestao.administracao_geral.views.remove_participante_interno import \
    remove_participante_interno
from gestao.administracao_geral.views.reunioes import reunioes

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^relatorio_reuniao/(?P<id_reuniao>\d+)/$', 
            admin.site.admin_view(relatorio_reuniao),
            name="relatorio_reuniao"),
    url(r'^remove_item_ata/(?P<id_item_ata>\d+)/$', 
            admin.site.admin_view(remove_item_ata),
            name="remove_item_ata"),
    url(r'^remove_participante_interno/(?P<id_participante_interno>\d+)/$', 
            admin.site.admin_view(remove_participante_interno),
            name="remove_participante_interno"),
    url(r'^remove_participante_externo/(?P<id_participante_externo>\d+)/$', 
            admin.site.admin_view(remove_participante_externo),
            name="remove_participante_externo"),
    url(r'^detalhes_reuniao/(?P<id_reuniao>\d+)/$', 
            admin.site.admin_view(detalhes_reuniao),
            name="detalhes_reuniao"),
    url(r'^reunioes/$', 
            admin.site.admin_view(reunioes),
            name="reunioes"),
    url(r'^editar_reuniao/(?P<id_reuniao>\d+)/$', 
            admin.site.admin_view(editar_reuniao),
            name="editar_reuniao"),
    url(r'^editar_reuniao/$', 
            admin.site.admin_view(editar_reuniao),
            name="editar_reuniao"),
    url(r'^editar_item_ata/(?P<id_reuniao>\d+)/(?P<id_item_ata>\d+)/$', 
            admin.site.admin_view(editar_item_ata),
            name="editar_item_ata"),
    url(r'^editar_item_ata/(?P<id_reuniao>\d+)/$', 
            admin.site.admin_view(editar_item_ata),
            name="editar_item_ata"),                       
    url(r'^editar_participante_interno/(?P<id_reuniao>\d+)/$', 
            admin.site.admin_view(editar_participante_interno),
            name="editar_participante_interno"),
    url(r'^editar_participante_externo/(?P<id_reuniao>\d+)/(?P<id_participante_externo>\d+)/$', 
            admin.site.admin_view(editar_participante_externo),
            name="editar_participante_externo"),
    url(r'^editar_participante_externo/(?P<id_reuniao>\d+)/$', 
            admin.site.admin_view(editar_participante_externo),
            name="editar_participante_externo"),    
    (r'^/', include(admin.site.urls)),
)