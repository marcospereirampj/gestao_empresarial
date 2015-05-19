# -*- coding: utf-8 -*-

from django.db import models

class Reuniao(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=200)     
    data_inicial = models.DateTimeField(verbose_name="Data de Início")
    data_final = models.DateTimeField(verbose_name="Data de Termino", blank=True, null=True)
    local = models.CharField(verbose_name="Local", max_length=200)
    encerrada = models.BooleanField(verbose_name="Reunião Encererrada?", default=False)
        
    def __unicode__(self):
        return u'%s' % (self.titulo)
                    
    class Meta:
        app_label = 'administracao_geral'
        verbose_name = 'Reunião'
        verbose_name_plural = 'Reuniões'
    
    
        