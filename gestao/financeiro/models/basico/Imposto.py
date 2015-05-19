# -*- coding: utf-8 -*-

from django.db import models
from gestao.financeiro.models.basico.TipoImposto import TipoImposto

class Imposto(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    tipo_de_imposto = models.ForeignKey(TipoImposto, verbose_name="Tipo de Imposto")    
    valor = models.DecimalField(verbose_name="Valor", help_text="Em porcentagem (%).",
                                max_digits=5, decimal_places=2, null=False, blank=False)
    
    def __unicode__(self):
        return u'%s' % (self.nome)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Imposto'
        verbose_name_plural = 'Imposto'