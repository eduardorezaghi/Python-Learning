import hr
import employees as emp
import productivity as prodc
import contacts as con

gerente = emp.Gerente(1, 'Marty Garrison', 3000)
gerente.endereco = con.Address(
    '121 Admin Road',
    'Concord',
    'NH',
    '03301'
)

secretaria = emp.Secretaria(2, 'Linda Lee', 1500)
secretaria.endereco = con.Address(
    '67 Paperwork Ave.',
    'Manchester',
    'NH',
    '03101'
)

vendedor = emp.Vendedor(3, 'John Roe', 1000, 250)
trab_fabrica = emp.TrabalhadorFabrica(4, 'Dan Quincy', 40, 15)
secretaria_temporaria = emp.SecretariaTemporaria(
    id=5, nome='Jane Killy', horas_trabalhadas=40, ganho_por_hora=9)

funcionarios = [
    gerente,
    secretaria,
    vendedor,
    trab_fabrica,
    secretaria_temporaria
]

sis_produtividade = prodc.SistemaProdutividade()
sis_produtividade.monitorar(funcionarios, 40)

sis_folha_pg = hr.FolhaDePagamento()

sis_folha_pg.calcular_folha(funcionarios)
