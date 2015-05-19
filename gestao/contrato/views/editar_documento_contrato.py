# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.contrato.models.documentos.ContratoDocumento import ContratoDocumento
from gestao.contrato.models.basico.Documento import Documento
from gestao.contrato.forms.DocumentoForm import DocumentoForm

def editar_documento_contrato( request, id_contrato, id_documento_contrato=None):
    
    title =  u"Editar Documento do Contrato"
    
    contrato = Contrato.objects.get(pk=id_contrato)
    
    if id_documento_contrato:
        documento_contrato = get_object_or_404(ContratoDocumento, pk=id_documento_contrato)
    else:
        documento_contrato = ContratoDocumento(contrato=contrato, documento=Documento())
        
    if request.method == 'POST':
        form_documento = DocumentoForm(request.POST,
                                       request.FILES, 
                                       instance=documento_contrato.documento)
                
        if form_documento.is_valid():
            documento = form_documento.save()
            documento_contrato.documento = documento
            documento_contrato.save()
    
            if '_save' in request.POST:
                return redirect('documentos_contrato', id_contrato=contrato.id)
            elif '_continue' in request.POST:
                return redirect('editar_documento_contrato', id_contrato=contrato.id, 
                                id_documento_contrato=documento_contrato.id)
            elif '_addanother' in request.POST:
                return redirect('editar_documento_contrato', id_contrato=contrato.id)
        
    else:
        form_documento = DocumentoForm(instance=documento_contrato.documento)        
            
    return render_to_response('editar_documento_contrato.html',locals(),
                              context_instance=RequestContext(request))