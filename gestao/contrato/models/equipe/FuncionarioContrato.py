# -*- coding: utf-8 -*-

from django.db import models
from gestao.contrato.models.contrato.Contrato import Contrato
from gestao.recursos_humanos.models.funcionario.Funcionario import Funcionario

class FuncionarioContrato(models.Model):
    contrato = models.ForeignKey(Contrato, verbose_name="Contrato")
    funcionario = models.ForeignKey(Funcionario, verbose_name="Funcionário")
    
    def __unicode__(self):
        return u'%s: %s' % (self.contrato.titulo, self.funcionario.nome_completo)
                    
    class Meta:
        app_label = 'contrato'
        verbose_name = 'Componente da Equipe'
        verbose_name_plural = 'Componentes da Equipe'
        unique_together = ('contrato', 'funcionario')
    
    
        