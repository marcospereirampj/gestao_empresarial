# -*- coding: utf-8 -*-

from django.contrib import admin
from gestao.recursos_humanos.admin_model.BeneficioAdmin import BeneficioAdmin
from gestao.recursos_humanos.admin_model.CargoAdmin import CargoAdmin
from gestao.recursos_humanos.admin_model.DependenteAdmin import DependenteAdmin
from gestao.recursos_humanos.admin_model.FuncionarioAdmin import \
    FuncionarioAdmin
from gestao.recursos_humanos.models.basico.Cargo import Cargo
from gestao.recursos_humanos.models.basico.DadosTrabalhista import \
    DadosTrabalhista
from gestao.recursos_humanos.models.beneficio.Beneficio import Beneficio
from gestao.recursos_humanos.models.dependente.Dependente import Dependente
from gestao.recursos_humanos.models.funcionario.Funcionario import Funcionario

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Dependente, DependenteAdmin)
admin.site.register(Beneficio, BeneficioAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(DadosTrabalhista)