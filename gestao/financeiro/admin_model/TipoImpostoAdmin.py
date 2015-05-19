# -*- coding: utf-8 -*-

from django.contrib import admin

class TipoImpostoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nome')
    list_display_links = ('codigo','nome')
    search_fields = ['nome','codigo']
    fieldsets = (
        ('', {
            'fields': (('nome',),)
        }),
    )