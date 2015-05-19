# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from gestao.financeiro.forms.PagamentoForm import PagamentoForm
from gestao.financeiro.models.movimentacoes.Despesa import Despesa
from gestao.financeiro.models.pagamento.Pagamento import Pagamento
from gestao.financeiro.models.pagamento.PagamentoDespesa import PagamentoDespesa

def realizar_pagamento_despesa(request, id_despesa):
    
    title =  u"Pagamento de Despesa"
        
    pagamento_despesa = PagamentoDespesa.objects.filter(despesa_id=id_despesa)
    
    if pagamento_despesa:
        pagamento_despesa = pagamento_despesa[0]
    else:
        despesa = get_object_or_404(Despesa, pk=id_despesa)
        pagamento = Pagamento()
        pagamento_despesa = PagamentoDespesa(despesa=despesa, pagamento=pagamento)
            
    if request.method == 'POST':
        form_pagamento = PagamentoForm(request.POST)
        
        if form_pagamento.is_valid():
            pagamento = form_pagamento.save()            
            pagamento_despesa.pagamento = pagamento
            pagamento_despesa.save()
        
        if '_save' in request.POST:
            return redirect('admin:financeiro_despesa_changelist')
    else:
        form_pagamento = PagamentoForm(instance=pagamento_despesa.pagamento)        

    return render_to_response('realizar_pagamento_despesa.html',locals(),
                              context_instance=RequestContext(request))