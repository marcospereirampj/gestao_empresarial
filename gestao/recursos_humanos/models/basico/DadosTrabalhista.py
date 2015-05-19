# -*- coding: utf-8 -*-

from django.db import models
from gestao.basico.models.localizacao.Cidade import Cidade

class DadosTrabalhista(models.Model):
    carteira_de_trabalho = models.CharField(verbose_name="Carteira de Trabalho", max_length=20)
    pis_pasep = models.CharField(verbose_name="PIS/PASEP", max_length=20, null=True, blank=True)
    data_de_admissao = models.DateField(verbose_name="Data de Admissão", 
                                          null=True, blank=True)
    cidade = models.ForeignKey(Cidade, verbose_name="Cidade de Trabalho", null=True, blank=True)
    
    def __unicode__(self):
        return u'CARTEIRA: %s, PIS/PASEP: %s, ADMISSÃO: %s' % (self.carteira_de_trabalho, 
                                            self.pis_pasep, 
                                            self.data_de_admissao)
                    
    class Meta:
        app_label = 'recursos_humanos'
        verbose_name = 'Dado Trabalhista'
        verbose_name_plural = 'Dados Trabalhistas'
    
    
        