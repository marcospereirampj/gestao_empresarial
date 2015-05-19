# -*- coding: utf-8 -*-

from django.db import models
from gestao.recursos_humanos.models.funcionario.Funcionario import Funcionario
from gestao.administracao_geral.models.reuniao.Reuniao import Reuniao

class ParticipanteInternoAta(models.Model):
    reuniao = models.ForeignKey(Reuniao, verbose_name="Ata")
    funcionario = models.ForeignKey(Funcionario, verbose_name="Funcionário")
        
    def __unicode__(self):
        return u'%s - /%s' % (self.reuniao.titulo, self.funcionario.nome_completo)
                    
    class Meta:
        app_label = 'administracao_geral'
        verbose_name = 'Participante Interno'
        verbose_name_plural = 'Participantes Internos'
        
        unique_together = ('reuniao', 'funcionario')