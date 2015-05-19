# -*- coding: utf-8 -*-

from gestao.basico.models.empresa.Empresa import Empresa

class DadosDaEmpresa(Empresa):
    
    def __unicode__(self):
        return u'%s - %s' % (self.razao_social, self.cnpj)
                    
    class Meta:
        app_label = 'administracao_geral'
        verbose_name = 'Dados da Empresa'
        verbose_name_plural = 'Dados das Empresas'
    
    
        