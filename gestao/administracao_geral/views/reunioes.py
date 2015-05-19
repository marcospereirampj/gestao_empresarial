# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from gestao.administracao_geral.models.reuniao.Reuniao import Reuniao

def reunioes( request):
    
    title =  u"Reuniões"
    
    reunioes = Reuniao.objects.all()
            
    return render_to_response('reunioes.html',locals(),
                              context_instance=RequestContext(request))