# -*- coding: utf-8 -*-

from django.forms.models import ModelForm
from gestao.contrato.models.equipe.FuncionarioContrato import FuncionarioContrato

class FuncionarioContratoForm(ModelForm):
    class Meta:
        model = FuncionarioContrato