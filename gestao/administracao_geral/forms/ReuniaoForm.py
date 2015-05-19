# -*- coding: utf-8 -*-

from django.forms.models import ModelForm
from gestao.administracao_geral.models.reuniao.Reuniao import Reuniao
from suit.widgets import SuitSplitDateTimeWidget

class ReuniaoForm(ModelForm):    
    class Meta:
        model = Reuniao
        widgets = {
            'data_inicial': SuitSplitDateTimeWidget,
        }