# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, redirect
from gestao.contrato.models.documentos.ContratoDocumento import ContratoDocumento

def remove_documento_contrato( request, id_documento_contrato):    
    documento = get_object_or_404(ContratoDocumento, pk=id_documento_contrato)
    id_contrato=documento.contrato.id
    documento.documento.delete()
    documento.delete()
    return redirect("documentos_contrato", id_contrato=id_contrato)   