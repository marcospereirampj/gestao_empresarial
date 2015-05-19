# -*- coding: utf-8 -*-

from django.forms.models import ModelForm
from gestao.financeiro.models.movimentacoes.Receita import Receita
from suit.widgets import SuitDateWidget

class ReceitaForm(ModelForm):
    class Meta:
        model = Receita
        widgets = {
            'data_prevista': SuitDateWidget,
        }        