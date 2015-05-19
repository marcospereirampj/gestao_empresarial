# -*- coding: utf-8 -*-

from django.db import models
from gestao.basico.models.localizacao.Endereco import Endereco

class Empresa(models.Model):
    nome_de_fantasia = models.CharField(verbose_name="Nome de Fantasia", max_length=200)
    razao_social = models.CharField(verbose_name="Razão Social", max_length=200)
    data_de_fundacao = models.DateField(verbose_name="Data de Fundação", 
                                          null=True, blank=True)
    cnpj = models.CharField(verbose_name="CNPJ", help_text="Somento números",
                           max_length=20, unique=True, null=False, blank=False)
        
    email = models.EmailField(verbose_name="Email", null=True, blank=True)
        
    telefone_principal = models.CharField(verbose_name="Telefone Principal",max_length=11,
                                        null=False, blank=False)
    
    telefone_secundario = models.CharField(verbose_name="Telefone Secundário", max_length=11,
                                     null=True, blank=True)
    
    endereco = models.ForeignKey(Endereco, verbose_name="Endereço",
                                 null=True, blank=True)
    
    ativo = models.BooleanField(verbose_name="Ativo?", default=True)
    
    def __unicode__(self):
        return u'%s - %s' % (self.nome_de_fantasia, self.cnpj)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    
        