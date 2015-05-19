# -*- coding: utf-8 -*-

from django.db import models
from gestao.contrato.models.basico.Documento import Documento
from gestao.contrato.models.contrato.Contrato import Contrato

class ContratoDocumento(models.Model):
    contrato = models.ForeignKey(Contrato, verbose_name="Contrato")
    documento = models.ForeignKey(Documento, verbose_name="Documento")
    
    def __unicode__(self):
        return u'%s: %s' % (self.contrato.titulo, self.documento.titulo)
                    
    class Meta:
        app_label = 'contrato'
        verbose_name = 'Documento do Contrato'
        verbose_name_plural = 'Documentos do Contrato'
    
    
        