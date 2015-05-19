# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.contrato.models.financeiro.ContratoDespesas import ContratoDespesas

def despesas_contrato( request, id_contrato):
    
    title =  u"Despesas do Contrato"
    
    contrato = get_object_or_404(Contrato, pk=id_contrato)
    
    despesas_dados = ContratoDespesas.objects.filter(contrato=contrato)
    
    total_a_faturar = 0
    total_pago = 0
    despesas_contrato = []
    
    for fat in despesas_dados:
        total_a_faturar += fat.despesa.valor_total
        
        pagamento_despesa = fat.pagamento()
        
        if pagamento_despesa:
            total_pago += pagamento_despesa.pagamento.valor_total
            despesas_contrato.append( ( fat, pagamento_despesa ) )
        else:
            despesas_contrato.append( ( fat, None ) )
            
    total_restante = total_a_faturar - total_pago
            
    return render_to_response('despesas_contrato.html',locals(),
                              context_instance=RequestContext(request))