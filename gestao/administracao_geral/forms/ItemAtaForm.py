# -*- coding: utf-8 -*-

from django.forms.models import ModelForm
from gestao.administracao_geral.models.reuniao.ItemAta import ItemAta

class ItemAtaForm(ModelForm):    
    class Meta:
        model = ItemAta