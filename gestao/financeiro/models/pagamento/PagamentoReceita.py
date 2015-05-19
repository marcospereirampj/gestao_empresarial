# -*- coding: utf-8 -*-

from django.db import models
from gestao.financeiro.models.movimentacoes.Receita import Receita
from gestao.financeiro.models.pagamento.Pagamento import Pagamento

class PagamentoReceita(models.Model):
    receita = models.ForeignKey(Receita, verbose_name="Receita", unique=True)
    pagamento = models.ForeignKey(Pagamento, verbose_name="Pagamento", unique=True)
    
    def __unicode__(self):
        return u'%s: %s ( %s )' % (self.receita.titulo, self.pagamento.valor_total, 
                                   self.pagamento.data)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Pagamento de Receita'
        verbose_name_plural = 'Pagamentos de Receitas'
    
    
        