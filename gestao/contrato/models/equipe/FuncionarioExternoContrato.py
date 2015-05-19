# -*- coding: utf-8 -*-

from django.db import models
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.contrato.models.equipe.FuncionarioExterno import FuncionarioExterno

class FuncionarioExternoContrato(models.Model):
    contrato = models.ForeignKey(Contrato, verbose_name="Contrato")
    funcionario_externo = models.ForeignKey(FuncionarioExterno, verbose_name="Funcionário Externo")
    
    def __unicode__(self):
        return u'%s' % (self.contrato.titulo, self.funcionario.nome_completo)
                    
    class Meta:
        app_label = 'contrato'
        verbose_name = 'Funcionário do Cliente'
        verbose_name_plural = 'Funcionários do Cliente'
        