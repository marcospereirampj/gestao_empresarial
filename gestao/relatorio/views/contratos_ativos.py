# -*- coding: utf-8 -*-

from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.relatorio.views.pdf import render_to_pdf_landscape

def contratos_ativos ( request ):
    
    contratos_ativos = Contrato.objects.all().order_by('id')
                
    context_dict = {
                'titulo' : "RELATÓRIO DE CONTRATOS ATIVOS",
                'contratos_ativos': contratos_ativos,             
                }
              
    return render_to_pdf_landscape('contratos_ativos.html', context_dict )