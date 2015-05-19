# -*- coding: utf-8 -*-

from gestao.basico.models.empresa.Empresa import Empresa

class Cliente(Empresa):
    
    def __unicode__(self):
        return u'%s' % (self.nome_de_fantasia)
                    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    
        