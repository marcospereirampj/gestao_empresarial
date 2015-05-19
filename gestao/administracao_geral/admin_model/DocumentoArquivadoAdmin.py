# -*- coding: utf-8 -*-

from django.contrib import admin

class DocumentoArquivadoAdmin(admin.ModelAdmin):
    list_display = ('documento','data_arquivamento')
    list_display_links = ('documento','data_arquivamento')
    search_fields = ['documento__titulo', 'documento__descricao']