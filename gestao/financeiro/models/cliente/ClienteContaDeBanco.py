# -*- coding: utf-8 -*-

from django.db import models
from gestao.financeiro.models.basico.ContaDeBanco import ContaDeBanco
from gestao.financeiro.models.cliente.Cliente import Cliente

class ClienteContaDeBanco(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente")
    dados_bancarios = models.ForeignKey(ContaDeBanco, verbose_name="Dados Bancários") 
    
    def __unicode__(self):
        return u'%s - %s' % (self.cliente.cnpj, self.dados_bancarios)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Conta Banc. do Cliente'
        verbose_name_plural = 'Contas Banc. do Cliente'
    
    
        