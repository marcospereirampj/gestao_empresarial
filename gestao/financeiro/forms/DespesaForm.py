# -*- coding: utf-8 -*-

from django.forms.models import ModelForm
from gestao.financeiro.models.movimentacoes.Despesa import Despesa
from suit.widgets import SuitDateWidget

class DespesaForm(ModelForm):
    class Meta:
        model = Despesa
        widgets = {
            'data_prevista': SuitDateWidget,
        }