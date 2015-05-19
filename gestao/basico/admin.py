# -*- coding: utf-8 -*-

from django.contrib import admin
from gestao.basico.models.formacao.Curso import Curso
from gestao.basico.models.formacao.Instituicao import Instituicao
from gestao.basico.models.localizacao.Cidade import Cidade
from gestao.basico.models.localizacao.Endereco import Endereco
from gestao.basico.models.localizacao.Estado import Estado
from gestao.basico.models.localizacao.Pais import Pais
from gestao.basico.models.pessoas.Parentesco import Parentesco

admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Instituicao)
admin.site.register(Curso)
admin.site.register(Parentesco)
admin.site.register(Endereco)