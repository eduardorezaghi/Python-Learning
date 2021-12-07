from hr import *
from employees import *
from productivity import *

gerente = Gerente(1, 'Marty Garrison', 3000)
secretaria = Secretaria(2, 'Linda Lee', 1500)
vendedor = Vendedor(3, 'John Roe', 1000, 250)
trab_fabrica = TrabalhadorFabrica(4, 'Dan Quincy', 40, 15)
secretaria_temporaria = SecretariaTemporaria(id=5, nome='Jane Killy', horas_trabalhadas=40, ganho_por_hora=9)

funcionarios = [
    gerente,
    secretaria,
    vendedor,
    trab_fabrica,
    secretaria_temporaria
]

sis_produtividade = SistemaProdutividade()
sis_produtividade.monitorar(funcionarios, 40)

sis_folha_pg = FolhaDePagamento()

sis_folha_pg.calcular_folha(funcionarios)