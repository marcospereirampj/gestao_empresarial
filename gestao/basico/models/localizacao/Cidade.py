# -*- coding: utf-8 -*-

from django.db import models
from gestao.basico.models.localizacao.Estado import Estado

class Cidade(models.Model):
      
    nome = models.CharField(verbose_name="Nome", max_length=200)
    sigla = models.CharField(verbose_name="Sigla", max_length=10)
    estado = models.ForeignKey(Estado, verbose_name="Estado")
        
    def __unicode__(self):
        return u'%s - %s' % (self.nome, self.estado)
                    
    class Meta:
        app_label = 'basico'
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
    
    
        