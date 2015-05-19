# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.contrato.models.documentos.ContratoDocumento import \
    ContratoDocumento
from gestao.contrato.models.equipe.FuncionarioContrato import \
    FuncionarioContrato
from gestao.contrato.models.financeiro.ContratoDespesas import ContratoDespesas
from gestao.contrato.models.financeiro.ContratoFaturamento import \
    ContratoFaturamento
from gestao.recursos_humanos.models.funcionario.FuncionarioCargo import \
    FuncionarioCargo

def detalhes_contrato( request, id_contrato):
    
    title =  u"Detalhes do Contrato"
    
    contrato = get_object_or_404(Contrato, pk=id_contrato)
    
    lista_documentos = ContratoDocumento.objects.filter(contrato=contrato)
    lista_despesas = ContratoDespesas.objects.filter(contrato=contrato)
    lista_faturamentos = ContratoFaturamento.objects.filter(contrato=contrato)
    list_funcionario = FuncionarioContrato.objects.filter(contrato=contrato)
    
    equipe = []
    
    for func in list_funcionario:
        cargos = FuncionarioCargo.objects.filter(funcionario=func).order_by("-data_inicial")
        
        if cargos:
            equipe.append( ( func, cargos[0] ) )
        else:
            equipe.append( ( func, None) )    
                
    return render_to_response('detalhes_contrato.html',locals(),
                              context_instance=RequestContext(request))