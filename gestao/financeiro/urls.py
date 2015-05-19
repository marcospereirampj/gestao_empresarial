# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from gestao.financeiro.views.realizar_pagamento_despesa import \
    realizar_pagamento_despesa
from gestao.financeiro.views.realizar_pagamento_receita import \
    realizar_pagamento_receita

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^realizar_pagamento_receita/(?P<id_receita>\d+)/$', 
            admin.site.admin_view(realizar_pagamento_receita),
            name="realizar_pagamento_receita"),                   
    url(r'^realizar_pagamento_despesa/(?P<id_despesa>\d+)/$', 
            admin.site.admin_view(realizar_pagamento_despesa),
            name="realizar_pagamento_despesa"),   
    (r'^/', include(admin.site.urls)),
)