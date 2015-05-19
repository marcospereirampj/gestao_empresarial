# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, redirect
from gestao.administracao_geral.models.reuniao.ItemAta import ItemAta

def remove_item_ata( request, id_item_ata):    
    item = get_object_or_404(ItemAta, pk=id_item_ata)
    id_reuniao = item.reuniao.id
    if item.reuniao.encerrada:
        return redirect("detalhes_reuniao", id_reuniao=id_reuniao)
    item.delete()
    return redirect("detalhes_reuniao", id_reuniao=id_reuniao)