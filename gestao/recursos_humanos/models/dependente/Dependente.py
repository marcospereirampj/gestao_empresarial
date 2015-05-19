# -*- coding: utf-8 -*-

from django.db import models
from gestao.basico.models.pessoas.Parentesco import Parentesco
from gestao.recursos_humanos.models.basico.Pessoa import Pessoa
from gestao.recursos_humanos.models.funcionario.Funcionario import Funcionario

class Dependente(Pessoa):
    titular = models.ForeignKey(Funcionario, verbose_name="Titular (Funcionário)")
    parentesco = models.ForeignKey(Parentesco, verbose_name="Parentesco")
    
    def __unicode__(self):
        return u'%s - %s' % (self.nome_completo, self.cpf)
                    
    class Meta:
        app_label = 'recursos_humanos'
        verbose_name = 'Dependente'
        verbose_name_plural = 'Dependentes'
    
    
        