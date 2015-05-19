# -*- coding: utf-8 -*-

from gestao.basico.models.empresa.Empresa import Empresa

class Fornecedor(Empresa):
    
    def __unicode__(self):
        return u'%s - %s' % (self.nome_de_fantasia, self.cnpj)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
    
    
        