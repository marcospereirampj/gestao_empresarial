# -*- coding: utf-8 -*-

from django.contrib import admin

class ContratoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo','data_inicio', 'data_final','detalhes_contrato')
    list_display_links = ('codigo', 'titulo',)
    search_fields = ['titulo','descricao', 'cliente__nome_de_fantasia', 'responsavel_externo__nome_completo']
    
    fieldsets = (
        ('Dados Gerais', {
            'fields': (('titulo'),
                       ('descricao'),
                       ('responsavel_interno'),)
        }),
        ('Dados do Cliente', {
            'fields': (('cliente'),
                       ('responsavel_externo'),)
        }),
        ('Período', {
            'fields': (('data_inicio',),
                       ('data_final',))
        }),
        ('Valores', {
            'fields': (('valor_total'),)
        }),
    )    
    
    def detalhes_contrato(self, obj):
        return """<a href="/contrato/detalhes_contrato/%d/"> 
                        <i class="icon-th-list" style="margin-right:4px;"/></i>Detalhes
                  </a>""" % (obj.pk)
    
    detalhes_contrato.short_description = "Detalhes"
    detalhes_contrato.allow_tags = True