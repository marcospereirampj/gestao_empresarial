# -*- coding: utf-8 -*-

from django.forms.models import ModelForm
from gestao.administracao_geral.models.reuniao.ParticipanteInternoAta import ParticipanteInternoAta

class ParticipanteInternoForm(ModelForm):
    class Meta:
        model = ParticipanteInternoAta