# -*- coding: utf-8 -*-

from django.contrib import admin

class DependenteAdmin(admin.ModelAdmin):
    list_display = ('titular','parentesco','cpf','nome_completo')
    list_display_links = ('titular','parentesco','cpf','nome_completo')
    search_fields = ['parentesco','cpf','rg','data_de_nascimento','nome_completo','email_pessoal']
    list_filter = ('parentesco__parentesco','sexo','naturalidade','nacionalidade')
    fieldsets = (
        ('Funcionário Titular', {
            'fields': ('titular', 'parentesco')
        }),
        ('Dados Pessoais', {
            'fields': (('nome_completo', 'sexo'), 
                       ('data_de_nascimento', 'estado_civil'),
                       ( 'naturalidade', 'nacionalidade',))
        }),
        ('Documentos', {
            'fields': ('cpf', ('rg', 'rg_orgao_emissor'), 'data_emissao')
        }),
        ('Contato', {
            'fields': (('telefone_celular', 'telefone_fixo'),
                       ('email_pessoal',),)
        }),
        ('Ativo?', {
            'fields': ('ativo',)
        })
    )