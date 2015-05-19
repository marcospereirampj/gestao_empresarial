# -*- coding: utf-8 -*-

from django.forms.models import ModelForm
from gestao.contrato.models.basico.Documento import Documento

class DocumentoForm(ModelForm):
    class Meta:
        model = Documento