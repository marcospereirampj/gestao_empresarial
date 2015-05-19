# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from gestao.administracao_geral.models.reuniao.Reuniao import Reuniao
from gestao.administracao_geral.models.reuniao.ParticipanteExternoAta import ParticipanteExternoAta
from gestao.administracao_geral.forms.ParticipanteExternoForm import ParticipanteExternoForm

def editar_participante_externo( request, id_reuniao, id_participante_externo=None):
    
    title =  u"Editar Participante Externo"

    reuniao = Reuniao.objects.get(pk=id_reuniao)    
    
    if id_participante_externo:
        participante_externo = ParticipanteExternoAta.objects.get(pk=id_participante_externo)
    else:
        participante_externo = ParticipanteExternoAta(reuniao = reuniao)
        
    if reuniao.encerrada:
        return redirect('reunioes')
    else:
        if request.method == 'POST':
            form_participante_externo = ParticipanteExternoForm(request.POST,
                                                            instance=participante_externo)
                    
            if form_participante_externo.is_valid():
                participante_externo = form_participante_externo.save()
                return redirect( 'detalhes_reuniao', id_reuniao=reuniao.id )

        else:
            form_participante_externo = ParticipanteExternoForm(instance=participante_externo)
            
    return render_to_response('editar_participante_externo.html',locals(),
                              context_instance=RequestContext(request))