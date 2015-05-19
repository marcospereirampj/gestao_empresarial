# -*- coding: utf-8 -*-

from django.db import models

from gestao.recursos_humanos.models.basico.Pessoa import Pessoa

class FuncionarioExterno(Pessoa):
    email_trabalho = models.EmailField(verbose_name="Email de Trabalho", unique=True)    
    outras_informacoes = models.TextField(verbose_name="Outras Informações", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.nome_completo)
                    
    class Meta:
        app_label = 'contrato'
        verbose_name = 'Funcionário Externo'
        verbose_name_plural = 'Funcionários Externo'
        ordering = ('nome_completo', )
    
    
        