# -*- coding: utf-8 -*-

from django.contrib import admin

class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome','salario_bruto')
    list_display_links = ('nome','salario_bruto')
    search_fields = ['nome','descricao']
    fieldsets = (
        ('Dados Gerais', {
            'fields': (('nome',),
                       ('descricao',),)
        }),
        ('Salário', {
            'fields': (('salario_bruto',),)
        }),
    )