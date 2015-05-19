# -*- coding: utf-8 -*-

from django.db import models
from gestao.financeiro.models.cliente.Cliente import Cliente

class Receita(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=200)
    descricao = models.TextField(verbose_name="Descrição")    
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente")
    data_prevista = models.DateField(verbose_name="Data Prevista de Pagamento", 
                                          null=False, blank=False)    
    valor_total = models.DecimalField(verbose_name="Valor Pago (R$)",
                                max_digits=15, decimal_places=2, 
                                null=False, blank=False)
    
    def __unicode__(self):
        return u'%s: %s' % (self.titulo, self.valor_total)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
    
    
        