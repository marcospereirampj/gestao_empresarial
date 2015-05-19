# -*- coding: utf-8 -*-

from django.db import models
from gestao.basico.models.localizacao.Endereco import Endereco
from gestao.financeiro.models.cliente.Cliente import Cliente

class ClienteEndereco(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente", unique=True)
    endereco = models.ForeignKey(Endereco, verbose_name="Endereço", unique=True)
    
    def __unicode__(self):
        return u'%s: %s' % (self.cliente.nome_de_fantasia, self.endereco.cep)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Endereço de Cliente'
        verbose_name_plural = 'Endereços de Clientes'
    
    
        