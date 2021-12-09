from typing import overload

class FolhaDePagamento():
    def calcular_folha(self, funcionarios):
        print('Calculando Folha de Pagamento')
        print('=============================')
        for funcionario in funcionarios:
            print(
                f"Pagamento para: {funcionario.id} - {funcionario.nome}")
            print(f"- Valor a ser pago: R$ {funcionario.calcular_folha():.2f}")
            if funcionario.endereco:
                print(' - Enviar para:') 
                print(funcionario.endereco)
            print('')

class PoliticaAssalariado:
    def __init__(self, salario_semanal):
        self.salario_semanal = salario_semanal

    def calcular_folha(self):
        return self.salario_semanal


class PoliticaPagoPorHora:
    def __init__(self, horas_trabalhadas, ganho_por_hora):
        self.horas_trabalhadas = horas_trabalhadas
        self.ganho_por_hora = ganho_por_hora

    def calcular_folha(self):
        return self.horas_trabalhadas * self.ganho_por_hora


class PoliticaComissionado(PoliticaAssalariado):
    def __init__(self, salario_semanal, comissao):
        super().__init__(salario_semanal)
        self.comissao = comissao

    def calcular_folha(self):
        fixo = super().calcular_folha()
        return fixo + self.comissao
