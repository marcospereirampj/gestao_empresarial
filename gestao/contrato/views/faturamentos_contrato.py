# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.contrato.models.financeiro.ContratoFaturamento import ContratoFaturamento

def faturamentos_contrato( request, id_contrato):
    
    title =  u"Faturamentos do Contrato"
    
    contrato = get_object_or_404(Contrato, pk=id_contrato)
    
    faturamentos_dados = ContratoFaturamento.objects.filter(contrato=contrato)
    
    total_a_faturar = 0
    total_pago = 0
    faturamentos = []
    
    for fat in faturamentos_dados:
        total_a_faturar += fat.receita.valor_total
        
        pagamento_receita = fat.pagamento()
        
        if pagamento_receita:
            total_pago += pagamento_receita.pagamento.valor_total
            faturamentos.append( ( fat, pagamento_receita ) )
        else:
            faturamentos.append( ( fat, None ) )
    
    total_restante = total_a_faturar - total_pago
            
    return render_to_response('faturamentos_contrato.html',locals(),
                              context_instance=RequestContext(request))