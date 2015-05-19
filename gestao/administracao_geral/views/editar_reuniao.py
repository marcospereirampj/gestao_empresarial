# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from gestao.administracao_geral.models.reuniao.Reuniao import Reuniao
from gestao.administracao_geral.forms.ReuniaoForm import ReuniaoForm
from datetime import datetime

def editar_reuniao( request, id_reuniao=None):
    
    title =  u"Editar Reunião"

    if id_reuniao:    
        reuniao = Reuniao.objects.get(pk=id_reuniao)
    else:
        reuniao = Reuniao()
    
    if reuniao.encerrada:
        return redirect('reunioes')
    else:
        if request.method == 'POST':
            form_reuniao = ReuniaoForm(request.POST, instance=reuniao)
                    
            if form_reuniao.is_valid():
                reuniao = form_reuniao.save()
                
                if reuniao.encerrada:
                    reuniao.data_final = datetime.now()
                    
                reuniao.save()
        
                if '_save' in request.POST:
                    return redirect('detalhes_reuniao', id_reuniao=reuniao.id)
                elif '_continue' in request.POST:
                    return redirect('editar_reuniao', id_reuniao=reuniao.id)
                elif '_addanother' in request.POST:
                    return redirect('editar_reuniao')
            
        else:
            form_reuniao = ReuniaoForm(instance=reuniao)
            
    return render_to_response('editar_reuniao.html',locals(),
                              context_instance=RequestContext(request))