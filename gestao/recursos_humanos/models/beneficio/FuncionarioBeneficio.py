# -*- coding: utf-8 -*-

from django.db import models
from gestao.recursos_humanos.models.funcionario.Funcionario import Funcionario
from gestao.recursos_humanos.models.beneficio.Beneficio import Beneficio

class FuncionarioBeneficio(models.Model):
    funcionario = models.ForeignKey(Funcionario, verbose_name="Funcionário")
    beneficio = models.ForeignKey(Beneficio, verbose_name="Benefício")
    
    def __unicode__(self):
        return u'%s' % (self.beneficio.nome)
                    
    class Meta:
        app_label = 'recursos_humanos'
        verbose_name = 'Benefício do Funcionário'
        verbose_name_plural = 'Benefícios do Funcionário'
        