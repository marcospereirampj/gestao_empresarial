# -*- coding: utf-8 -*-

from django.db import models
from gestao.contrato.models.basico.TipoDocumento import TipoDocumento

class Documento(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=200)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    tipo_de_documento = models.ForeignKey(TipoDocumento, verbose_name="Tipo")
    arquivo = models.FileField(verbose_name="Arquivo", 
                               upload_to="documentos/",
                               null=True, blank=True)
    
    def __unicode__(self):
        return u'%s - %s - %s' % (self.titulo, self.tipo_de_documento.nome, self.arquivo)
                    
    class Meta:
        app_label = 'contrato'
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
    
    
        