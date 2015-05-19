# -*- coding: utf-8 -*-

from django.db import models
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.financeiro.models.movimentacoes.Despesa import Despesa
from gestao.financeiro.models.pagamento.PagamentoDespesa import PagamentoDespesa

class ContratoDespesas(models.Model):
    contrato = models.ForeignKey(Contrato, verbose_name="Contrato")
    despesa = models.ForeignKey(Despesa, verbose_name="Despesa")
    
    def __unicode__(self):
        return u'%s: %s' % (self.contrato.titulo, self.despesa.valor_total)
    
    def pagamento(self):
        pagamento_despesa = PagamentoDespesa.objects.filter(despesa=self.despesa)        
        if pagamento_despesa:
            return pagamento_despesa[0]
        return None
                    
    class Meta:
        app_label = 'contrato'
        verbose_name = 'Despesa do Contrato'
        verbose_name_plural = 'Despesas do Contrato'
    
    
        