# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, redirect
from gestao.contrato.models.financeiro.ContratoDespesas import ContratoDespesas

def remove_despesa_contrato( request, id_despesa_contrato):    
    despesa_contrato = get_object_or_404(ContratoDespesas, pk=id_despesa_contrato)    
    id_contrato=despesa_contrato.contrato.id
    despesa_contrato.despesa.delete()
    despesa_contrato.delete()
    return redirect("despesas_contrato", id_contrato=id_contrato)   