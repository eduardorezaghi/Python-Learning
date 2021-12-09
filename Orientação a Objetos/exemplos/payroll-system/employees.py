from hr import (
    PoliticaAssalariado,
    PoliticaPagoPorHora,
    PoliticaComissionado
)

from productivity import (
    FuncaoGerencia,
    FuncaoSecretaria,
    FuncaoVendas,
    FuncaoFabrica
)

class Funcionario():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.endereco = None

# SISTEMA DE PRODUTIVIDADE


class Gerente(Funcionario, FuncaoGerencia, PoliticaAssalariado):
    def __init__(self, id, nome, salario_semanal):
        PoliticaAssalariado.__init__(self, salario_semanal)
        super().__init__(id, nome)


class Secretaria(Funcionario, FuncaoSecretaria, PoliticaAssalariado):
    def __init__(self, id, nome, salario_semanal):
        PoliticaAssalariado.__init__(self, salario_semanal)
        super().__init__(id, nome)


class Vendedor(Funcionario, FuncaoVendas, PoliticaComissionado):
    def __init__(self, id, nome, salario_semanal, comissao):
        PoliticaComissionado.__init__(self, salario_semanal, comissao)
        super().__init__(id, nome)



class TrabalhadorFabrica(Funcionario, FuncaoFabrica, PoliticaPagoPorHora):
    def __init__(self, id, nome, horas_trabalhadas, ganho_por_hora):
        PoliticaPagoPorHora.__init__(self, horas_trabalhadas, ganho_por_hora)
        super().__init__(id, nome)


# HERANÇA MÚLTIPLA
class SecretariaTemporaria(Funcionario, FuncaoSecretaria, PoliticaPagoPorHora):
    def __init__(self, id, nome, horas_trabalhadas, ganho_por_hora):
        PoliticaPagoPorHora.__init__(self,horas_trabalhadas, ganho_por_hora)
        super().__init__(id, nome)
