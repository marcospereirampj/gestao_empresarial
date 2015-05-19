# -*- coding: utf-8 -*-

from django.contrib import admin
from gestao.financeiro.admin_model.ClienteAdmin import ClienteAdmin
from gestao.financeiro.admin_model.DespesaAdmin import DespesaAdmin
from gestao.financeiro.admin_model.FornecedorAdmin import FornecedorAdmin
from gestao.financeiro.admin_model.ReceitaAdmin import ReceitaAdmin
from gestao.financeiro.models.basico.Banco import Banco
from gestao.financeiro.models.basico.ContaDeBanco import ContaDeBanco
from gestao.financeiro.models.basico.Imposto import Imposto
from gestao.financeiro.models.basico.TipoDespesa import TipoDespesa
from gestao.financeiro.models.basico.TipoImposto import TipoImposto
from gestao.financeiro.models.cliente.Cliente import Cliente
from gestao.financeiro.models.fornecedor.Fornecedor import Fornecedor
from gestao.financeiro.models.movimentacoes.Despesa import Despesa
from gestao.financeiro.models.movimentacoes.Receita import Receita
from gestao.financeiro.admin_model.TipoDespesaAdmin import TipoDespesaAdmin
from gestao.financeiro.admin_model.TipoImpostoAdmin import TipoImpostoAdmin

admin.site.register(Banco)
admin.site.register(ContaDeBanco)
admin.site.register(Imposto)
admin.site.register(TipoDespesa, TipoDespesaAdmin)
admin.site.register(TipoImposto, TipoImpostoAdmin)

admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Fornecedor, FornecedorAdmin)

admin.site.register(Despesa, DespesaAdmin)
admin.site.register(Receita, ReceitaAdmin)