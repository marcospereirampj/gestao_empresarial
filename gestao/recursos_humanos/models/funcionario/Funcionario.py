# -*- coding: utf-8 -*-

from django.db import models
from gestao.basico.models.localizacao.Endereco import Endereco
from gestao.financeiro.models.basico.ContaDeBanco import ContaDeBanco
from gestao.recursos_humanos.models.basico.DadosTrabalhista import \
    DadosTrabalhista
from gestao.recursos_humanos.models.basico.Pessoa import Pessoa

class Funcionario(Pessoa):
    #matricula = models.CharField(verbose_name="Matrícula", max_length=200)
    email_trabalho = models.EmailField(verbose_name="Email de Trabalho", unique=True)    
    endereco = models.ForeignKey(Endereco, verbose_name="Endereço", null=True, blank=True)        
    dados_trabalhista = models.ForeignKey(DadosTrabalhista, verbose_name="Dados Trabalhista", 
                                          null=True, blank=True, unique=True)
    conta_bancaria = models.ForeignKey(ContaDeBanco, verbose_name="Conta Bancária", 
                                       null=True, blank=True, unique=True)
    
    def __unicode__(self):
        return u'%s' % (self.nome_completo)
                    
    class Meta:
        app_label = 'recursos_humanos'
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ('nome_completo', )
    
    
        