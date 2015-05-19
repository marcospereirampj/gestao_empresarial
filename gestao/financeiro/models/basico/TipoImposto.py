# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_save

class TipoImposto(models.Model):      
    nome = models.CharField(verbose_name="Nome", max_length=200)
    codigo = models.CharField(verbose_name="Código", max_length=10, unique=True)
        
    def __unicode__(self):
        return u'%s - %s' % (self.nome, self.codigo)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Tipo de Imposto'
        verbose_name_plural = 'Tipos de Impostos'
        
        
def tipo_imposto_post_save(sender, instance, created, **kwargs):
    if created:
        instance.codigo = "TP" + str(instance.id)
        instance.save()
        
post_save.connect(tipo_imposto_post_save, sender=TipoImposto)  
    
    
        