# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from gestao.financeiro.forms.PagamentoForm import PagamentoForm
from gestao.financeiro.models.movimentacoes.Receita import Receita
from gestao.financeiro.models.pagamento.Pagamento import Pagamento
from gestao.financeiro.models.pagamento.PagamentoReceita import PagamentoReceita

def realizar_pagamento_receita(request, id_receita):
    
    title =  u"Pagamento de Receita"
        
    pagamento_receita = PagamentoReceita.objects.filter(receita_id=id_receita)
    
    if pagamento_receita:
        pagamento_receita = pagamento_receita[0]
    else:
        receita = get_object_or_404(Receita, pk=id_receita)
        pagamento = Pagamento()
        pagamento_receita = PagamentoReceita(receita=receita, pagamento=pagamento)
            
    if request.method == 'POST':
        form_pagamento = PagamentoForm(request.POST)
        
        if form_pagamento.is_valid():
            pagamento = form_pagamento.save()            
            pagamento_receita.pagamento = pagamento
            pagamento_receita.save()

        if '_save' in request.POST:
            return redirect('admin:financeiro_receita_changelist')  
                  
    else:
        form_pagamento = PagamentoForm(instance=pagamento_receita.pagamento)        

    return render_to_response('realizar_pagamento_receita.html',locals(),
                              context_instance=RequestContext(request))