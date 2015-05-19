# -*- coding: utf-8 -*-

from django.db import models
from gestao.financeiro.models.basico.ContaDeBanco import ContaDeBanco
from gestao.financeiro.models.fornecedor.Fornecedor import Fornecedor

class FornecedorContaDeBanco(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, verbose_name="Cliente")
    dados_bancarios = models.ForeignKey(ContaDeBanco, verbose_name="Dados Bancários") 
    
    def __unicode__(self):
        return u'%s - %s' % (self.fornecedor.cnpj, self.dados_bancarios)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Conta Banc. do Fornecedor'
        verbose_name_plural = 'Contas Banc. do Fornecedor'
    
    
        