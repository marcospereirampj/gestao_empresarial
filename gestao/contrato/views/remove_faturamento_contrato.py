# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, redirect
from gestao.contrato.models.financeiro.ContratoFaturamento import \
    ContratoFaturamento

def remove_faturamento_contrato( request, id_faturamento_contrato):    
    faturamento = get_object_or_404(ContratoFaturamento, pk=id_faturamento_contrato)
    id_contrato=faturamento.contrato.id
    faturamento.receita.delete()
    faturamento.delete()
    return redirect("faturamentos_contrato", id_contrato=id_contrato)   