# -*- coding: utf-8 -*-

from django.contrib import admin
from gestao.financeiro.models.pagamento.PagamentoReceita import PagamentoReceita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('titulo','cliente', 'valor_total', 'realizar_pagamento')
    list_display_links = ('titulo','cliente', 'valor_total')
    search_fields = ['titulo','cliente__nomde_de_fantasia','valor_total']
    fieldsets = (
        ('Dados Gerais', {
            'fields': ('titulo', 'descricao')
        }),
        ('Cliente', {
            'fields': ('cliente',)
        }),
        ('Valores', {
            'fields': ('data_prevista', 'valor_total')
        }),
    )
    
    def realizar_pagamento(self, obj):
        pagamento_receita = PagamentoReceita.objects.filter(receita=obj)
        
        if pagamento_receita: 
            pagamento_receita = pagamento_receita[0]
            link = """<a href="/financeiro/realizar_pagamento_receita/%d/">
                            <i class="icon-ok"/></i> ( Pagamento Realizado: R$ %0.2f )</a>"""
                            
            return  link % (obj.pk, pagamento_receita.pagamento.valor_total)
        else:
            return """<a href="/financeiro/realizar_pagamento_receita/%d/">
                        <i class="icon-plus"></i> ( Adicionar Pagamento ) </a>""" % (obj.pk)
    
    realizar_pagamento.short_description = "Pagamento Realizado?"
    realizar_pagamento.allow_tags = True