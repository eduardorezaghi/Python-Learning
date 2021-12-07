class FolhaDePagamento():
    def calcular_folha(self, funcionarios):
        print('Calculando Folha de Pagamento')
        print('=============================')
        for funcionario in funcionarios:
            print(
                f"Folha de Pagamento para: {funcionario.id} - {funcionario.nome}")
            print(f"- Valor a ser pago: {funcionario.calcular_folha()}")
            print('')


class Funcionario():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def trabalhar():
        pass


class FuncionarioAssalariado(Funcionario):
    def __init__(self, id, nome, salario_semanal):
        super().__init__(id, nome)
        self.salario_semanal = salario_semanal

    def calcular_folha(self):
        return self.salario_semanal
