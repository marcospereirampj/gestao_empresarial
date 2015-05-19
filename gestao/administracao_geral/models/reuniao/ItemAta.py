# -*- coding: utf-8 -*-

from django.db import models
from gestao.administracao_geral.models.reuniao.Reuniao import Reuniao

class ItemAta(models.Model):
    reuniao = models.ForeignKey(Reuniao, verbose_name="Ata")
    descricao = models.TextField(verbose_name="Descrição", null=False, blank=False)
    
    def __unicode__(self):
        return u'%s: %s' % (self.reuniao.titulo, self.titulo)
                    
    class Meta:
        app_label = 'administracao_geral'
        verbose_name = 'Item da Ata'
        verbose_name_plural = 'Itens da Ata'
    
    
        