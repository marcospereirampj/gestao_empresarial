# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, redirect
from gestao.administracao_geral.models.reuniao.ParticipanteInternoAta import ParticipanteInternoAta

def remove_participante_interno( request, id_participante_interno):    
    participante = get_object_or_404(ParticipanteInternoAta, pk=id_participante_interno)
    id_reuniao = participante.reuniao.id
    if participante.reuniao.encerrada:
        return redirect("detalhes_reuniao", id_reuniao=id_reuniao)
    participante.delete()
    return redirect("detalhes_reuniao", id_reuniao=id_reuniao)