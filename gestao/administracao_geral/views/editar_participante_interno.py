# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from gestao.administracao_geral.forms.ParticipanteInternoForm import \
    ParticipanteInternoForm
from gestao.administracao_geral.models.reuniao.ParticipanteInternoAta import \
    ParticipanteInternoAta
from gestao.administracao_geral.models.reuniao.Reuniao import Reuniao

def editar_participante_interno( request, id_reuniao):
    
    title =  u"Editar Participante Interno"

    reuniao = Reuniao.objects.get(pk=id_reuniao)
    participantes = ParticipanteInternoAta.objects.filter(reuniao=reuniao)    
            
    if reuniao.encerrada:
        return redirect('reunioes')
    else:
        if request.method == 'POST':                    
            form_participante_interno = ParticipanteInternoForm(request.POST)
                    
            if form_participante_interno.is_valid():
                participante_interno = form_participante_interno.save()
                return redirect( 'detalhes_reuniao', id_reuniao=reuniao.id )
        else:
            form_participante_interno = ParticipanteInternoForm()
            
    return render_to_response('editar_participante_interno.html',locals(),
                              context_instance=RequestContext(request))