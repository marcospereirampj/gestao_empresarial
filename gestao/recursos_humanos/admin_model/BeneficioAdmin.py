# -*- coding: utf-8 -*-

from django.contrib import admin

class BeneficioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome','valor_para_titular','valor_para_dependente')
    list_display_links = ('codigo','nome','valor_para_titular','valor_para_dependente')
    search_fields = ['nome','codigo']
    fieldsets = (
        ('Dados Gerais', {
            'fields': (('nome',),
                       ('descricao'),)
        }),
        ('Valores', {
            'fields': (('valor_para_titular',),
                       ( 'valor_para_dependente'))
        }),
    )