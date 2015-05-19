# -*- coding: utf-8 -*-

from django.contrib import admin

class TipoDespesaAdmin(admin.ModelAdmin):
    list_display = ('codigo','nome')
    list_display_links = ('codigo','nome')
    search_fields = ['nome','codigo']
    fieldsets = (
        ('', {
            'fields': (('nome',),)
        }),
    )