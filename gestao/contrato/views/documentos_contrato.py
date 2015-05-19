# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.contrato.models.documentos.ContratoDocumento import \
    ContratoDocumento

def documentos_contrato( request, id_contrato):
    
    title =  u"Documentos do Contrato"
    
    contrato = get_object_or_404(Contrato, pk=id_contrato)
    
    documentos_dados = ContratoDocumento.objects.filter(contrato=contrato)
                    
    return render_to_response('documentos_contrato.html',locals(),
                              context_instance=RequestContext(request))