# -*- coding: utf-8 -*-

from django.contrib import admin
from gestao.administracao_geral.admin_model.DadosEmpresaAdmin import \
    DadosDaEmpresaAdmin
from gestao.administracao_geral.admin_model.DocumentoArquivadoAdmin import \
    DocumentoArquivadoAdmin
from gestao.administracao_geral.models.documentos.DocumentoArquivado import \
    DocumentoArquivado
from gestao.administracao_geral.models.empresa.DadosDaEmpresa import \
    DadosDaEmpresa

admin.site.register(DadosDaEmpresa, DadosDaEmpresaAdmin)
admin.site.register(DocumentoArquivado, DocumentoArquivadoAdmin)