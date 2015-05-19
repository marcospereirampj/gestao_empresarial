#-*- coding: utf-8 -*-

# Django settings for gestao project.

from decimal import ROUND_HALF_EVEN

from moneyed.localization import _FORMATTER
import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

USE_THOUSAND_SEPARATOR = True
DECIMAL_SEPARATOR = ","
THOUSAND_SEPARATOR = "."
NUMBER_GROUPING = 3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'gestao/media/gestao_db.sqlite',
    }
}


ALLOWED_HOSTS = []

TIME_ZONE = 'America/Maceio'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True

USE_L10N = False

MEDIA_ROOT = PROJECT_ROOT_PATH + '/media/'

MEDIA_URL = '/media/'

STATIC_ROOT = '/static/'

STATIC_URL = '/static/'

FORMAT_MODULE_PATH = 'formats'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'a_)-ge%fuyx*95pih0t9azv45ktroca(r4k$nwyw4mx&hg-t1f'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'gestao.urls'

WSGI_APPLICATION = 'gestao.wsgi.application'

ADMIN_TOOLS_MENU = 'gestao.menu.CustomMenu'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH,'templates'),
)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_COOKIE_AGE = 86400

SUIT_CONFIG = {
    'ADMIN_NAME': 'Sistema de Gestão Empresarial',
    'LIST_PER_PAGE': 10,
    'CONFIRM_UNSAVED_CHANGES': False,
    'HEADER_DATE_FORMAT': 'd/m/Y',
    'HEADER_TIME_FORMAT': 'H:i',
    'SEARCH_URL': '',
    'MENU_OPEN_FIRST_CHILD': True,  
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,      
    'MENU': (            

            # Separator
            '-',
                  
            {'label': u'Administração Geral',
                'icon':'icon-book',
                'permissions': 'administracao_geral.add_reuniao',
                'models': ('administracao_geral.dadosdaempresa',
                           {'label': 'Reuniões', 'url' : '/administracao_geral/reunioes/'},
                           'administracao_geral.documentoarquivado')},
             
            # Separator
            '-',             
                  
            {'label': 'Recursos Humanos',
                'icon':'icon-user', 
                'permissions': 'recursos_humanos.change_funcionario',
                'models': ('recursos_humanos.funcionario','recursos_humanos.dependente', 
                           'recursos_humanos.beneficio',
                           'recursos_humanos.cargo')},

            # Separator
            '-',             
                  
            {'label': 'Financeiro',
                'icon':'icon-briefcase',
                'permissions': 'contrato.add_pagamento', 
                'models': ('financeiro.cliente','financeiro.fornecedor', 
                           'financeiro.despesa','financeiro.receita',)},

            # Separator
            '-',             
                  
            {'label': 'Contratos',
                'icon':'icon-file',
                'permissions': 'contrato.add_contrato', 
                'models': ('contrato.contrato',)},

    
            # Separator
            '-',
            
            {'label': 'Acessos', 'permissions': 'auth.add_user',
                'icon':'icon-lock', 'models': ('auth.user', 'auth.group')},

            # Separator
            '-',
             
            {'label': u'Básicos', 
                'icon':'icon-cog',
                'permissions': 'recursos_humanos.add_endereco',                
                'models': ('basico.endereco','basico.cidade',
                           'basico.estado','basico.pais',
                           'basico.banco','basico.curso',
                           'basico.instituicao','basico.parentesco',
                           'financeiro.tipodespesa', 'financeiro.tipoimposto', 
                           'contrato.tipodocumento', 'financeiro.imposto'),
             },
        )    
}

CURRENCIES = ('BRL','USD',)

_FORMATTER.add_formatting_definition(
    'default', group_size=3, group_separator=".", decimal_point=",",
    positive_sign="",  trailing_positive_sign="",
    negative_sign="-", trailing_negative_sign="",
    rounding_method=ROUND_HALF_EVEN)

#adminmedia

INSTALLED_APPS = (
    'suit',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'gestao.basico',
    'gestao.recursos_humanos',
    'gestao.financeiro',
    'gestao.contrato',
    'gestao.administracao_geral',
    'gestao.relatorio', 
)


input_formats = ['%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
'%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
'%Y-%m-%d',              # '2006-10-25'
'%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
'%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
'%m/%d/%Y',              # '10/25/2006'
'%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
'%m/%d/%y %H:%M',        # '10/25/06 14:30'
'%m/%d/%y']              # '10/25/06'


DATETIME_FORMAT = 'd/m/Y H:i'

DATE_FORMAT = 'd/m/Y'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
