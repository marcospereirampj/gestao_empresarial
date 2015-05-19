# -*- coding: utf-8 -*-

from django.contrib import admin

class ReuniaoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_inicial', 'data_final','local')
    list_display_links = ('titulo',)
    search_fields = ['titulo','local']
    
    fieldsets = (
        ('Dados Gerais', {
            'fields': (('titulo'),
                       ('data_inicial'),
                       ('data_final'),
                       ('local'))
        }),
    )