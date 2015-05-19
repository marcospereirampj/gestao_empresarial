# -*- coding: utf-8 -*-

from django.db import models
from gestao.basico.models.localizacao.Pais import Pais

class Estado(models.Model):
      
    nome = models.CharField(verbose_name="Nome", max_length=200)
    sigla = models.CharField(verbose_name="Sigla", max_length=10)
    pais = models.ForeignKey(Pais, verbose_name="País")
   
    def __unicode__(self):
        return u'%s' % (self.nome)
                    
    class Meta:
        app_label = 'basico'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
    
    
        