# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from gestao.administracao_geral.models.reuniao.ParticipanteExternoAta import \
    ParticipanteExternoAta
from gestao.administracao_geral.models.reuniao.ParticipanteInternoAta import \
    ParticipanteInternoAta
from gestao.administracao_geral.models.reuniao.Reuniao import Reuniao
from gestao.administracao_geral.models.reuniao.ItemAta import ItemAta

def detalhes_reuniao( request, id_reuniao ):
    
    title =  u"Detalhes de Reunião"
    
    reuniao = get_object_or_404(Reuniao, pk=id_reuniao)    
    lista_participantes_externo = ParticipanteExternoAta.objects.filter(reuniao=reuniao)    
    lista_participantes_interno = ParticipanteInternoAta.objects.filter(reuniao=reuniao)
    itens_ata = ItemAta.objects.filter(reuniao=reuniao)

    return render_to_response('detalhes_reuniao.html',locals(),
                              context_instance=RequestContext(request))