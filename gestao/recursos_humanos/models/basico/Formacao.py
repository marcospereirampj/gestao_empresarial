# -*- coding: utf-8 -*-

from django.db import models
from gestao.basico.models.formacao.Curso import Curso
from gestao.recursos_humanos.models.funcionario.Funcionario import Funcionario

class Formacao(models.Model):
    funcionario = models.ForeignKey(Funcionario, verbose_name="Funcionário")
    curso = models.ForeignKey(Curso, verbose_name="Curso")
    ano = models.IntegerField(verbose_name="Ano de Formação")
    
    def __unicode__(self):
        return u' %s : %s (%s)' % (self.funcionario.nome_completo, self.curso, self.ano)
                    
    class Meta:
        app_label = 'recursos_humanos'
        verbose_name = 'Formação'
        verbose_name_plural = 'Formações'
        