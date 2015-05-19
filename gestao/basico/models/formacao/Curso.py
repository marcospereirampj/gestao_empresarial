# -*- coding: utf-8 -*-

from django.db import models
from gestao.basico.models.formacao.Instituicao import Instituicao

TITULOS = ( ( 'BACHAREL', 'BACHAREL' ),
            ( 'LICENCIATURA', 'LICENCIATURA' ),
            ( 'MESTRE', 'MESTRE' ),
            ( 'DOUTOR', 'DOUTOR') )

class Curso(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    titulo = models.CharField(verbose_name="Título obtido", max_length=30, 
                                    choices=TITULOS, null=False, blank=False)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    instituicao = models.ForeignKey(Instituicao, verbose_name="Instituição de Ensino")
    
    def __unicode__(self):
        return u'%s' % (self.nome)
                    
    class Meta:
        app_label = 'basico'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
    
    
        