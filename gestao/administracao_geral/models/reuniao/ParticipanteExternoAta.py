# -*- coding: utf-8 -*-

from django.db import models
from gestao.administracao_geral.models.reuniao.Reuniao import Reuniao
from gestao.basico.models.empresa.Empresa import Empresa

class ParticipanteExternoAta(models.Model):
    reuniao = models.ForeignKey(Reuniao, verbose_name="Ata")
    nome_completo = models.CharField(verbose_name="Nome Completo", max_length=300)
    cargo = models.CharField(verbose_name="Cargo", max_length=300)
    empresa = models.ForeignKey(Empresa, verbose_name="Empresa")
        
    def __unicode__(self):
        return u'%s (%s/%s)' % (self.nome_completo, self.cargo, self.empresa.nome_de_fantasia)
                    
    class Meta:
        app_label = 'administracao_geral'
        verbose_name = 'Participante Externo'
        verbose_name_plural = 'Participantes Externos'
    
    
        