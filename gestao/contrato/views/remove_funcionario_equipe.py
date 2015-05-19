# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, redirect
from gestao.contrato.models.equipe.FuncionarioContrato import FuncionarioContrato

def remove_funcionario_equipe( request, id_funcionario):    
    integrante = get_object_or_404(FuncionarioContrato, funcionario=id_funcionario)
    id_contrato=integrante.contrato.id
    integrante.delete()
    return redirect("equipe_contrato", id_contrato=id_contrato)   