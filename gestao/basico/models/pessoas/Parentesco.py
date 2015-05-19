# -*- coding: utf-8 -*-

from django.db import models

class Parentesco(models.Model):      
    parentesco = models.CharField(verbose_name="Parentesco", max_length=200)
        
    def __unicode__(self):
        return u'%s' % (self.parentesco)
                    
    class Meta:
        app_label = 'basico'
        verbose_name = 'Parentesco'
        verbose_name_plural = 'Parentescos'
    
    
        