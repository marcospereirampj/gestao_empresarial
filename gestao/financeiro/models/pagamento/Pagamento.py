# -*- coding: utf-8 -*-

from django.db import models

class Pagamento(models.Model):    
    data = models.DateField(verbose_name="Data de Pagamento", 
                                          null=False, blank=False)
    valor_total = models.DecimalField(verbose_name="Valor Pago (R$)" , 
                                max_digits=15, decimal_places=2,
                                null=False, blank=False)
    realizado = models.BooleanField(verbose_name="Pagamento Realizado?", default=True)    
    
    def __unicode__(self):
        return u'%s: R$ %s' % (self.data, self.valor_total)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
    
    
        