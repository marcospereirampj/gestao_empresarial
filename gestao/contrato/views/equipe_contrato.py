# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.contrato.models.equipe.FuncionarioContrato import FuncionarioContrato
from gestao.recursos_humanos.models.funcionario.FuncionarioCargo import FuncionarioCargo
from gestao.contrato.forms.FuncionarioContratoForm import FuncionarioContratoForm


def equipe_contrato( request, id_contrato):
    
    title =  u"Equipe do Contrato"
    
    contrato = get_object_or_404(Contrato, pk=id_contrato)
    
    equipe_dado = FuncionarioContrato.objects.filter(contrato=contrato)
    
    funcionario_contrato = FuncionarioContrato(contrato=contrato)
        
    if request.method == "POST":      
        form_equipe_contrato = FuncionarioContratoForm(request.POST,
                                                       instance=funcionario_contrato)        
        if form_equipe_contrato.is_valid():
            form_equipe_contrato.save()
            funcionario_contrato = FuncionarioContrato(contrato=contrato)            
            form_equipe_contrato = FuncionarioContratoForm(instance=funcionario_contrato)                                 
    else:
        form_equipe_contrato = FuncionarioContratoForm(instance=funcionario_contrato)

    equipe = []
    
    for func in equipe_dado:
        cargos = FuncionarioCargo.objects.filter(funcionario=func).order_by("-data_inicial")
        
        if cargos:        
            equipe.append( ( func, cargos[0] ) )
        else:
            equipe.append( ( func, None) )
                
    return render_to_response('equipe_contrato.html',locals(),
                              context_instance=RequestContext(request))