# -*- coding: utf-8 -*-

from django.db import models

class Pais(models.Model):
      
    nome = models.CharField(verbose_name="Nome", max_length=200)
    sigla = models.CharField(verbose_name="Sigla", max_length=10)
        
    def __unicode__(self):
        return u'%s - %s' % (self.nome, self.sigla)
                    
    class Meta:
        app_label = 'basico'
        verbose_name = 'País'
        verbose_name_plural = 'Países'
    
    
        