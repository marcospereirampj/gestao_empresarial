# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_save

class TipoDocumento(models.Model):      
    nome = models.CharField(verbose_name="Nome", max_length=200)
    codigo = models.CharField(verbose_name="Código", max_length=10, unique=True)
        
    def __unicode__(self):
        return u'%s - %s' % (self.nome, self.codigo)
                    
    class Meta:
        app_label = 'contrato'
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'
    
def tipo_documento_post_save(sender, instance, created, **kwargs):
    if created:
        instance.codigo = "TDOC" + str(instance.id)
        instance.save()
post_save.connect(tipo_documento_post_save, sender=TipoDocumento)
    
        