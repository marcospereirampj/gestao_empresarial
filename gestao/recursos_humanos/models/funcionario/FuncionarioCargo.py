# -*- coding: utf-8 -*-

from django.db import models
from gestao.recursos_humanos.models.basico.Cargo import Cargo
from gestao.recursos_humanos.models.funcionario.Funcionario import Funcionario

class FuncionarioCargo(models.Model):
    funcionario = models.ForeignKey(Funcionario, verbose_name="Funcionário")
    cargo = models.ForeignKey(Cargo, verbose_name="Cargo")
    data_inicial = models.DateField(verbose_name="Data de Início", null=True, blank=True)
    data_final = models.DateField(verbose_name="Data Final", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.cargo.nome)
                    
    class Meta:
        app_label = 'recursos_humanos'
        verbose_name = 'Cargo do Funcionário'
        verbose_name_plural = 'Cargos dos Funcionários'
        