# -*- coding: utf-8 -*-

from django.db import models
from gestao.financeiro.models.movimentacoes.Despesa import Despesa
from gestao.financeiro.models.pagamento.Pagamento import Pagamento

class PagamentoDespesa(models.Model):
    despesa = models.ForeignKey(Despesa, verbose_name="Despesa")
    pagamento = models.ForeignKey(Pagamento, verbose_name="Pagamento")
    
    def __unicode__(self):
        return u'%s: %s' % (self.despesa.titulo, self.pagamento.data)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Pagamento de Despesa'
        verbose_name_plural = 'Pagamentos de Despesas'
    
    
        