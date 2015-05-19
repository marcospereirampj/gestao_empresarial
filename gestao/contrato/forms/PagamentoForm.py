# -*- coding: utf-8 -*-

from django.forms.models import ModelForm
from gestao.financeiro.models.pagamento.Pagamento import Pagamento

class PagamentoForm(ModelForm):
    class Meta:
        model = Pagamento