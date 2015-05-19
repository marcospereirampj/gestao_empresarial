# -*- coding: utf-8 -*-

from django.db import models
from gestao.basico.models.localizacao.Cidade import Cidade

class Instituicao(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    cidade = models.ForeignKey(Cidade, verbose_name="Cidade")
    
    def __unicode__(self):
        return u'%s' % (self.nome)
                    
    class Meta:
        app_label = 'basico'
        verbose_name = 'Instituição de Ensino'
        verbose_name_plural = 'Instituíções de Ensino'
    
    
        