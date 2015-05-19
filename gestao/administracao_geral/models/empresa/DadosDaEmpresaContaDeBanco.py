# -*- coding: utf-8 -*-

from django.db import models
from gestao.administracao_geral.models.empresa.DadosDaEmpresa import \
    DadosDaEmpresa
from gestao.financeiro.models.basico.ContaDeBanco import ContaDeBanco

class DadosDaEmpresaContaDeBanco(models.Model):
    dados_da_empresa = models.ForeignKey(DadosDaEmpresa, verbose_name="Dados Da Empresa")
    dados_bancarios = models.ForeignKey(ContaDeBanco, verbose_name="Dados Bancários") 
    
    def __unicode__(self):
        return u'%s - %s' % (self.dados_da_empresa.cnpj, self.dados_bancarios)
                    
    class Meta:
        app_label = 'administracao_geral'
        verbose_name = 'Conta Banc. da Empresa'
        verbose_name_plural = 'Contas Banc. da Empresas'
    
    
        