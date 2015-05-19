# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.contrato.models.financeiro.ContratoDespesas import ContratoDespesas
from gestao.financeiro.forms.DespesaForm import DespesaForm
from gestao.financeiro.models.movimentacoes.Despesa import Despesa

def editar_despesa_contrato( request, id_contrato, id_despesa_contrato=None):
    
    title =  u"Editar Faturamentos do Contrato"
    
    contrato = Contrato.objects.get(pk=id_contrato)
    
    if id_despesa_contrato:
        despesa_contrato = get_object_or_404(ContratoDespesas, pk=id_despesa_contrato)
    else:
        despesa_contrato = ContratoDespesas(contrato=contrato,despesa=Despesa())
        
    if request.method == 'POST':
        form_despesa = DespesaForm(request.POST, instance=despesa_contrato.despesa)
                
        if form_despesa.is_valid():
            despesa = form_despesa.save()
            despesa_contrato.despesa = despesa
            despesa_contrato.save()
    
            if '_save' in request.POST:
                return redirect('despesas_contrato', id_contrato=contrato.id)
            elif '_continue' in request.POST:
                return redirect('editar_despesa_contrato', id_contrato=contrato.id, 
                                id_despesa_contrato=despesa_contrato.id)
            elif '_addanother' in request.POST:
                return redirect('editar_despesa_contrato', id_contrato=contrato.id)
        
    else:
        form_despesa = DespesaForm(instance=despesa_contrato.despesa)        
            
    return render_to_response('editar_despesa_contrato.html',locals(),
                              context_instance=RequestContext(request))