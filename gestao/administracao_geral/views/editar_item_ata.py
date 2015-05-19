# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from gestao.administracao_geral.models.reuniao.Reuniao import Reuniao
from gestao.administracao_geral.models.reuniao.ItemAta import ItemAta
from gestao.administracao_geral.forms.ItemAtaForm import ItemAtaForm

def editar_item_ata( request, id_reuniao, id_item_ata=None):
    
    title =  u"Editar Item da Ata"

    reuniao = Reuniao.objects.get(pk=id_reuniao)

    if id_item_ata:    
        item_ata = ItemAta.objects.get(pk=id_item_ata)
    else:
        item_ata = ItemAta(reuniao=reuniao)
    
    if reuniao.encerrada:
        return redirect('reunioes')
    else:
        if request.method == 'POST':
            form_item_ata = ItemAtaForm(request.POST, instance=item_ata)
                    
            if form_item_ata.is_valid():
                item_ata = form_item_ata.save()
        
                if '_save' in request.POST:
                    return redirect('detalhes_reuniao', id_reuniao=reuniao.id)
                elif '_continue' in request.POST:
                    return redirect('editar_item_ata', id_reuniao=reuniao.id, id_item_ata=item_ata.id)
                elif '_addanother' in request.POST:
                    return redirect('editar_item_ata', id_reuniao=reuniao.id)
            
        else:
            form_item_ata = ItemAtaForm(instance=item_ata)
            
    return render_to_response('editar_item_ata.html',locals(),
                              context_instance=RequestContext(request))