# -*- coding: utf-8 -*-

from django.contrib import admin
from gestao.administracao_geral.models.empresa.DadosDaEmpresaContaDeBanco import \
    DadosDaEmpresaContaDeBanco

class DadosDaEmpresaContaDeBancoInline(admin.TabularInline):
    fieldsets = (
        ('', {
            'fields': ('dados_bancarios',)
        }),
    )    
    model = DadosDaEmpresaContaDeBanco

class DadosDaEmpresaAdmin(admin.ModelAdmin):
    list_display = ('cnpj','nome_de_fantasia','telefone_principal')
    list_display_links = ('cnpj','nome_de_fantasia','telefone_principal')
    search_fields = ['cnpj','nomde_de_fantasia','razao_social','email','telefone_principal']
    inlines = [DadosDaEmpresaContaDeBancoInline,]
    fieldsets = (
        ('Dados Gerais', {
            'fields': (('cnpj', 'nome_de_fantasia'), 
                       ('razao_social', 'data_de_fundacao'))
        }),
        ('Endereço', {
            'fields': ('endereco',)
        }),                 
        ('Contato', {
            'fields': (('email', 'telefone_principal'),
                       ('telefone_secundario',),)
        }),
        ('Ativo?', {
            'fields': ('ativo',)
        })
    )