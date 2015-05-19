# -*- coding: utf-8 -*-

from django.contrib import admin
from gestao.recursos_humanos.models.basico.Formacao import Formacao
from gestao.recursos_humanos.models.funcionario.FuncionarioCargo import FuncionarioCargo
from gestao.recursos_humanos.models.beneficio.FuncionarioBeneficio import FuncionarioBeneficio

class FuncionarioBeneficioInline(admin.TabularInline):
    fieldsets = (
        ('', {
            'fields': ('beneficio',)
        }),
    )    
    model = FuncionarioBeneficio
    suit_classes = 'suit-tab suit-tab-beneficios'

class FuncionarioCargoInline(admin.TabularInline):
    fieldsets = (
        ('', {
            'fields': (('cargo',),
                       ('data_inicial','data_final'))
        }),
    )    
    model = FuncionarioCargo
    suit_classes = 'suit-tab suit-tab-cargos'

class FormacaoInline(admin.TabularInline):
    fieldsets = (
        ('', {
            'fields': (('curso', 'ano'))
        }),
    )    
    model = Formacao
    suit_classes = 'suit-tab suit-tab-formacao'

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome_completo')
    list_display_links = ('cpf', 'nome_completo')
    search_fields = ['cpf', 'nome_completo', 'email_trabalho', 'email_pessoal']
    list_filter = ('sexo', 'naturalidade', 'nacionalidade')
    inlines = [FormacaoInline, FuncionarioCargoInline, FuncionarioBeneficioInline]
    fieldsets = (
        ('Dados Pessoais', {
            'classes': ('suit-tab suit-tab-geral',),                            
            'fields': (('nome_completo', 'sexo'), 
                       ('data_de_nascimento', 'estado_civil'),
                       ( 'naturalidade', 'nacionalidade',))
        }),
        ('Documentos', {
            'classes': ('suit-tab suit-tab-geral',),
            'fields': ('cpf', ('rg', 'rg_orgao_emissor'), 'data_emissao')
        }),
        ('Endereço', {
            'classes': ('suit-tab suit-tab-geral',),                      
            'fields': ('endereco',)
        }),                 
        ('Contato', {
            'classes': ('suit-tab suit-tab-geral',),                     
            'fields': (('email_trabalho', 'email_pessoal'),
                       ('telefone_celular', 'telefone_fixo'))
        }),
        ('Ativo?', {
            'classes': ('suit-tab suit-tab-geral',),
            'fields': ('ativo',)
        }),
        ('Dados Bancários', {
            'classes': ('suit-tab suit-tab-dadosbancarios',),
            'fields': ('conta_bancaria',)
        }),
        ('Dados Trabalhista', {
            'classes': ('suit-tab suit-tab-dadostrabalhista',),
            'fields': ('dados_trabalhista',)
        }),                 
    )
    
    suit_form_tabs = (('geral', 'Geral'), 
                      ('dadosbancarios', u'Dados Bancários'),
                      ('dadostrabalhista', u'Dados Trabalhista'),
                      ('cargos', u'Cargos Ocupados'),
                      ('formacao', u'Formação'),
                      ('beneficios', u'Benefícios'),)
    