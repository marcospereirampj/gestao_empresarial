# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, redirect
from gestao.administracao_geral.models.reuniao.ParticipanteExternoAta import ParticipanteExternoAta

def remove_participante_externo( request, id_participante_externo):
    participante = get_object_or_404(ParticipanteExternoAta, pk=id_participante_externo)
    id_reuniao = participante.reuniao.id
    if participante.reuniao.encerrada:
        return redirect("detalhes_reuniao", id_reuniao=id_reuniao)
    participante.delete()
    return redirect("detalhes_reuniao", id_reuniao=id_reuniao)