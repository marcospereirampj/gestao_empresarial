# -*- coding: utf-8 -*-

from django.db import models
from gestao.financeiro.models.basico.TipoDespesa import TipoDespesa
from gestao.financeiro.models.fornecedor.Fornecedor import Fornecedor

class Despesa(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=200)
    descricao = models.TextField(verbose_name="Descrição")
    fornecedor = models.ForeignKey(Fornecedor, verbose_name="Fornecedor",
                                   null=False, blank=False)
    
    data_prevista = models.DateField(verbose_name="Data Prevista de Pagamento", 
                                          null=False, blank=False)
    
    tipo_de_despesa = models.ForeignKey(TipoDespesa, verbose_name="Tipo")
    
    valor_total = models.DecimalField(verbose_name="Valor Pago (R$)",
                                max_digits=15, decimal_places=2,
                                null=False, blank=False)
    
    def __unicode__(self):
        return u'%s: %s' % (self.titulo, self.valor_total)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
    
    
        