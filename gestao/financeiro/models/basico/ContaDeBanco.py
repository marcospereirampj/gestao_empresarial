# -*- coding: utf-8 -*-

from django.db import models
from gestao.financeiro.models.basico.Banco import Banco

class ContaDeBanco(models.Model):
    agencia = models.CharField(verbose_name="Agência", max_length=10)
    conta_corrente = models.CharField(verbose_name="Conta Corrente", max_length=15)
    operacao = models.CharField(verbose_name="Operação", max_length=5, null=True, blank=True)
    banco = models.ForeignKey(Banco, verbose_name="Banco")
    
    def __unicode__(self):
        return u'BANCO: %s, AG: %s, CC: %s' % (self.banco, self.agencia, self.conta_corrente)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Conta do Banco'
        verbose_name_plural = 'Contas de Banco'
        unique_together = ("agencia", "conta_corrente", "banco")
    
    
        