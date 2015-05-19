# -*- coding: utf-8 -*-

from django.db import models
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.financeiro.models.movimentacoes.Receita import Receita
from gestao.financeiro.models.pagamento.PagamentoReceita import PagamentoReceita

class ContratoFaturamento(models.Model):
    contrato = models.ForeignKey(Contrato, verbose_name="Contrato")
    receita = models.ForeignKey(Receita, verbose_name="Receita")
    
    def pagamento(self):
        pagamento_receita = PagamentoReceita.objects.filter(receita=self.receita)        
        if pagamento_receita:
            return pagamento_receita[0]
        return None    
    
    def __unicode__(self):
        return u'%s: %s' % (self.contrato.titulo, self.receita.valor_total)
                    
    class Meta:
        app_label = 'contrato'
        verbose_name = 'Faturamento do Contrato'
        verbose_name_plural = 'Faturamento do Contrato'
    
    
        