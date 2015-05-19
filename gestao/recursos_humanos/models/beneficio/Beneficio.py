# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_save


class Beneficio(models.Model):      
    nome = models.CharField(verbose_name="Nome", max_length=200)
    codigo = models.CharField(verbose_name="Código", max_length=200)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    
    valor_para_titular = models.DecimalField(verbose_name="Valor para funcionário (R$)",
                                max_digits=15, decimal_places=2,
                                null=True, blank=True)
        
    valor_para_dependente = models.DecimalField(verbose_name="Valor para dependente (R$)",
                                max_digits=15, decimal_places=2,
                                null=True, blank=True)    
    
    def __unicode__(self):
        return u'%s' % (self.nome)
                    
    class Meta:
        app_label = 'recursos_humanos'
        verbose_name = 'Benefício'
        verbose_name_plural = 'Benefícios'
        
def beneficio_post_save(sender, instance, created, **kwargs):
    if created:
        instance.codigo = "BN" + str(instance.id)
        instance.save()
post_save.connect(beneficio_post_save, sender=Beneficio)
    
    
        