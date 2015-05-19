# -*- coding: utf-8 -*-

from django.db import models

class Cargo(models.Model):      
    nome = models.CharField(verbose_name="Nome", max_length=200)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    salario_bruto = models.DecimalField(verbose_name="Salário Bruto (R$)",
                                max_digits=15, decimal_places=2,
                                null=True, blank=True,)
        
    def __unicode__(self):
        return u'%s' % (self.nome)
                    
    class Meta:
        app_label = 'recursos_humanos'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'