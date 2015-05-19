# -*- coding: utf-8 -*-

from django.forms.models import ModelForm
from gestao.administracao_geral.models.reuniao.ParticipanteExternoAta import ParticipanteExternoAta

class ParticipanteExternoForm(ModelForm):
    class Meta:
        model = ParticipanteExternoAta