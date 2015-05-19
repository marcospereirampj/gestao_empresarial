# -*- coding: utf-8 -*-

from django.contrib import admin
from gestao.contrato.admin_model.ContratoAdmin import ContratoAdmin
from gestao.contrato.admin_model.TipoDocumentoAdmin import TipoDocumentoAdmin
from gestao.contrato.models.basico.Documento import Documento
from gestao.contrato.models.basico.TipoDocumento import TipoDocumento
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.contrato.models.documentos.ContratoDocumento import \
    ContratoDocumento
from gestao.contrato.models.equipe.FuncionarioExterno import FuncionarioExterno
from gestao.contrato.models.equipe.FuncionarioExternoContrato import \
    FuncionarioExternoContrato

admin.site.register(Contrato, ContratoAdmin)
admin.site.register(ContratoDocumento)
admin.site.register(FuncionarioExternoContrato)
admin.site.register(FuncionarioExterno)
admin.site.register(Documento)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)