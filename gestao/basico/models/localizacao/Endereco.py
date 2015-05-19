# -*- coding: utf-8 -*-

from django.db import models
from gestao.basico.models.localizacao.Cidade import Cidade

class Endereco(models.Model):     
    logradouro = models.TextField(verbose_name="Logradouro")
    bairro = models.CharField(verbose_name="Bairro", max_length=25)
    cep = models.CharField(verbose_name="CEP", max_length=15)    
    cidade = models.ForeignKey(Cidade, verbose_name="Cidade")
        
    def __unicode__(self):
        return u'%s - %s - %s - %s' % (self.logradouro, self.bairro, self.cidade, self.cep)
                    
    class Meta:
        app_label = 'basico'
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
    
    
        