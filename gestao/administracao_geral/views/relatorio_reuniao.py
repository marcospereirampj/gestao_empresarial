# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from gestao.administracao_geral.models.reuniao.ItemAta import ItemAta
from gestao.administracao_geral.models.reuniao.ParticipanteExternoAta import \
    ParticipanteExternoAta
from gestao.administracao_geral.models.reuniao.ParticipanteInternoAta import \
    ParticipanteInternoAta
from gestao.administracao_geral.models.reuniao.Reuniao import Reuniao
from gestao.relatorio.views.pdf import render_to_pdf

def relatorio_reuniao( request, id_reuniao):
    
    reuniao = get_object_or_404(Reuniao, pk=id_reuniao)    
    lista_participantes_externo = ParticipanteExternoAta.objects.filter(reuniao=reuniao)    
    lista_participantes_interno = ParticipanteInternoAta.objects.filter(reuniao=reuniao)
    itens_ata = ItemAta.objects.filter(reuniao=reuniao)
                
    context_dict = {
                'titulo' : "RELATÓRIO - REUNIÃO",
                'reuniao': reuniao,
                'lista_participantes_externo': lista_participantes_externo,
                'lista_participantes_interno': lista_participantes_interno,
                'itens_ata': itens_ata }
              
    return render_to_pdf('relatorio_reuniao.html', context_dict )