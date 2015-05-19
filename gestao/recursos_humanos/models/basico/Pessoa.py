# -*- coding: utf-8 -*-

from django.db import models

SEXO = ( ('MASCULINO', 'MASCULINO'),
         ('FEMININO' , 'FEMININO') )

ESTADO_CIVIL = ( ( 'SOLTEIRO(A)', 'SOLTEIRO(A)' ),
                 ( 'CASADO(A)', 'CASADO(A)' ),
                 ( 'DIVORCIADO(A)', 'DIVORCIADO(A)' ),
                 ( 'VIUVO(A)', 'VIÚVO(A)') )

class Pessoa(models.Model):
    nome_completo = models.CharField(verbose_name="Nome Completo", max_length=200)
    data_de_nascimento = models.DateField(verbose_name="Data de Nascimento", 
                                          null=True, blank=True)
    sexo = models.CharField(verbose_name="Sexo", max_length=30, choices=SEXO)
    
    nacionalidade = models.CharField(verbose_name="Nacionalidade", max_length=100, 
                                     null=True, blank=True)
    naturalidade = models.CharField(verbose_name="Naturalidade", max_length=100, 
                                    null=True, blank=True)
    estado_civil = models.CharField(verbose_name="Estado Civil", max_length=30, 
                                    choices=ESTADO_CIVIL, null=True, blank=True)
        
    cpf = models.CharField(verbose_name="CPF", help_text="Somente números.",
                           max_length=11, unique=True, null=False, blank=False)
    
    rg = models.CharField(verbose_name="RG", max_length=20, null=True, blank=True)
    rg_orgao_emissor = models.CharField(verbose_name="Órgão Emissor do RG",
                                        max_length=20, null=True, blank=True)
    data_emissao = models.DateField(verbose_name="Data de Emissão do RG", null=True, blank=True)
    
    email_pessoal = models.EmailField(verbose_name="Email Pessoal", 
                                      null=True, blank=True)
        
    telefone_celular = models.CharField(verbose_name="Telefone Celular",max_length=11,
                                        null=True, blank=True)
    telefone_fixo = models.CharField(verbose_name="Telefone Fixo", max_length=11,
                                     null=True, blank=True)
            
    ativo = models.BooleanField(verbose_name="Ativo?", default=True)
    
    def __unicode__(self):
        return u'%s - %s' % (self.nome_completo, self.cpf)
                    
    class Meta:
        abstract = True
        app_label = 'recursos_humanos'
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
    
    
        