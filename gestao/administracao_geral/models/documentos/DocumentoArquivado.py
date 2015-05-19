# -*- coding: utf-8 -*-

from django.db import models
from gestao.contrato.models.basico.Documento import Documento

class DocumentoArquivado(models.Model):  
    documento = models.ForeignKey(Documento, verbose_name="Documento")    
    data_arquivamento = models.DateField(verbose_name="Data de Arquivamento")
        
    def __unicode__(self):
        return u'%s - %s' % (self.documento.titulo, self.data_arquivamento)
                    
    class Meta:
        app_label = 'administracao_geral'
        verbose_name = 'Documento Arquivado'
        verbose_name_plural = 'Documentos Arquivados'
    
    
        