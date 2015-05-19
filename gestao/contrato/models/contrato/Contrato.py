# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_save
from gestao.contrato.models.equipe.FuncionarioExterno import FuncionarioExterno
from gestao.financeiro.models.cliente.Cliente import Cliente
from gestao.recursos_humanos.models.funcionario.Funcionario import Funcionario
import datetime

class Contrato(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=200)
    titulo = models.CharField(verbose_name="Título", max_length=200)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)    
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente")
    responsavel_interno = models.ForeignKey(Funcionario, verbose_name="Responsável Interno",
                                            null=True, blank=True)
    responsavel_externo = models.ForeignKey(FuncionarioExterno, verbose_name="Responsável Externo",
                                            null=True, blank=True)
    valor_total = models.DecimalField(verbose_name="Valor Total do Contrato (R$)",
                                max_digits=15, decimal_places=2, 
                                null=True, blank=True)
    data_inicio = models.DateField(verbose_name="Data de Início", 
                                          null=False, blank=False)
    data_final = models.DateField(verbose_name="Data de Término", 
                                          null=False, blank=False)
    
    def __unicode__(self):
        return u'%s' % (self.titulo,)
                    
    class Meta:
        app_label = 'contrato'
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        
def contrato_post_save(sender, instance, created, **kwargs):
    if created:
        instance.codigo = "%05d/%d" % (instance.id, datetime.datetime.now().year)
        instance.save()
        
post_save.connect(contrato_post_save, sender=Contrato)
    
    
        