# -*- coding: utf-8 -*-

from django.db import models
from gestao.recursos_humanos.models.beneficio.Beneficio import Beneficio
from gestao.recursos_humanos.models.dependente.Dependente import Dependente

class DependenteBeneficio(models.Model):
    dependente = models.ForeignKey(Dependente, verbose_name="Dependente")
    beneficio = models.ForeignKey(Beneficio, verbose_name="Benefício")
    
    def __unicode__(self):
        return u'%s' % (self.beneficio.nome)
                    
    class Meta:
        app_label = 'recursos_humanos'
        verbose_name = 'Benefício do Dependente'
        verbose_name_plural = 'Benefícios do Dependente'
        