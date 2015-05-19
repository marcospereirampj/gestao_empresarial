# -*- coding: utf-8 -*-

from django.db import models
from gestao.basico.models.localizacao.Cidade import Cidade

class Banco(models.Model):      
    nome = models.CharField(verbose_name="Nome", max_length=200)
    codigo = models.CharField(verbose_name="Código", max_length=10, unique=True)
    cidade = models.ForeignKey(Cidade, verbose_name="Cidade")
        
    def __unicode__(self):
        return u'%s - %s' % (self.nome, self.cidade)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
    
    
        