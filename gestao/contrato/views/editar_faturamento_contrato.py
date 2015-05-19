# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.contrato.models.financeiro.ContratoFaturamento import \
    ContratoFaturamento
from gestao.financeiro.forms.ReceitaForm import ReceitaForm
from gestao.financeiro.models.movimentacoes.Receita import Receita

def editar_faturamento_contrato( request, id_contrato, id_faturamento_contrato=None):
    
    title =  u"Editar Faturamentos do Contrato"
    
    contrato = Contrato.objects.get(pk=id_contrato)
    
    if id_faturamento_contrato:
        faturamento_contrato = get_object_or_404(ContratoFaturamento, pk=id_faturamento_contrato)
    else:
        faturamento_contrato = ContratoFaturamento(contrato=contrato,receita=Receita(cliente=contrato.cliente))
        
    if request.method == 'POST':
        form_receita = ReceitaForm(request.POST, instance=faturamento_contrato.receita)
                
        if form_receita.is_valid():
            receita = form_receita.save()
            faturamento_contrato.receita = receita
            faturamento_contrato.save()
    
            if '_save' in request.POST:
                return redirect('faturamentos_contrato', id_contrato=contrato.id)
            elif '_continue' in request.POST:
                return redirect('editar_faturamento_contrato', id_contrato=contrato.id, 
                                id_faturamento_contrato=faturamento_contrato.id)
            elif '_addanother' in request.POST:
                return redirect('editar_faturamento_contrato', id_contrato=contrato.id)
        
    else:
        form_receita = ReceitaForm(instance=faturamento_contrato.receita)        
            
    return render_to_response('editar_faturamento_contrato.html',locals(),
                              context_instance=RequestContext(request))