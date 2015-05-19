# -*- coding: utf-8 -*-

import cgi
import datetime

from django import http
from django.http import HttpResponse
from django.template import Context, loader
from xhtml2pdf import pisa

import cStringIO as StringIO
from gestao.settings import PROJECT_ROOT_PATH


def render_to_pdf(template_src, context_dict):
    data_atual = datetime.datetime.now()
    context_dict['data_atual'] = data_atual 
    context_dict['project_root'] = PROJECT_ROOT_PATH
    template = loader.get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
        
    css = open(PROJECT_ROOT_PATH + '/static/admin/css/pisa.css').read()
            
    pdf = pisa.CreatePDF(StringIO.StringIO(html.encode("utf-8")), result, default_css=css)
    
    if not pdf.err:
        response = HttpResponse(result.getvalue(), mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=relatorio_' + str(data_atual) + ".pdf"
        return response
    return http.HttpResponse('We had some errors<pre>%s</pre>' % cgi.escape(html))

def render_to_pdf_landscape(template_src, context_dict):
    data_atual = datetime.datetime.now()
    context_dict['data_atual'] = data_atual
    context_dict['project_root'] = PROJECT_ROOT_PATH
    template = loader.get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
        
    css_retrato = open(PROJECT_ROOT_PATH + '/static/admin/css/pisa_landscape.css').read()
        
    pdf = pisa.CreatePDF(StringIO.StringIO(html.encode("utf-8")), result, default_css=css_retrato)
    
    if not pdf.err:
        response = HttpResponse(result.getvalue(), mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=relatorio_' + str(data_atual) + ".pdf"
        return response
    return http.HttpResponse('We had some errors<pre>%s</pre>' % cgi.escape(html))
