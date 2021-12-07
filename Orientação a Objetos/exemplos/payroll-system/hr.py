from typing import overload
from employees import *


class FolhaDePagamento():
    def calcular_folha(self, funcionarios):
        print('Calculando Folha de Pagamento')
        print('=============================')
        for funcionario in funcionarios:
            print(
                f"Pagamento para: {funcionario.id} - {funcionario.nome}")
            print(f"- Valor a ser pago: R$ {funcionario.calcular_folha():.2f}")
            print('')
