# -*- coding: utf-8 -*-

from django.contrib import admin
from gestao.financeiro.models.pagamento.PagamentoDespesa import PagamentoDespesa

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('titulo','fornecedor','tipo_de_despesa', 'valor_total', 'realizar_pagamento')
    list_display_links = ('titulo','fornecedor','tipo_de_despesa', 'valor_total')
    search_fields = ['titulo','fornecedor__nomde_de_fantasia','valor_total','tipo_de_despesa__nome']
    list_filter = ('tipo_de_despesa__nome',)
    fieldsets = (
        ('Dados Gerais', {
            'fields': ('titulo', 'descricao','tipo_de_despesa')
        }),
        ('Fornecedor', {
            'fields': ('fornecedor',)
        }),
        ('Valores', {
            'fields': ('data_prevista', 'valor_total')
        }),
    )
    
    def realizar_pagamento(self, obj):
        pagamento_despesa = PagamentoDespesa.objects.filter(despesa=obj)
        
        if pagamento_despesa: 
            pagamento_despesa = pagamento_despesa[0]
            link = """<a href="/financeiro/realizar_pagamento_despesa/%d/">
                            <i class="icon-ok"/></i> ( Pagamento Realizado: R$ %0.2f )</a>"""
                            
            return  link % (obj.pk, pagamento_despesa.pagamento.valor_total)
        else:
            return """<a href="/financeiro/realizar_pagamento_despesa/%d/">
                        <i class="icon-plus"></i> ( Adicionar Pagamento ) </a>""" % (obj.pk)
    
    realizar_pagamento.short_description = "Pagamento Realizado?"
    realizar_pagamento.allow_tags = True    