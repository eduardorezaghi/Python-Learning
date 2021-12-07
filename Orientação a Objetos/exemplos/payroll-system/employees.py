class Funcionario():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class FuncionarioAssalariado(Funcionario):
    def __init__(self, id, nome, salario_semanal):
        super().__init__(id, nome)
        self.salario_semanal = salario_semanal

    def calcular_folha(self):
        return self.salario_semanal


class FuncionarioPagoPorHora(Funcionario):
    def __init__(self, id, nome, horas_trabalhadas, ganho_por_hora):
        super().__init__(id, nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.ganho_por_hora = ganho_por_hora

    def calcular_folha(self):
        return self.horas_trabalhadas * self.ganho_por_hora


class FuncionarioComissionado(FuncionarioAssalariado):
    def __init__(self, id, nome, salario_semanal, comissao):
        super().__init__(id, nome, salario_semanal)
        self.comissao = comissao

    def calcular_folha(self):
        fixo = super().calcular_folha()
        return fixo + self.comissao


# SISTEMA DE PRODUTIVIDADE


class Gerente(FuncionarioAssalariado):
    def trabalhar(self, horas):
        print(f"{self.nome} grita e xinga por {horas} horas.")


class Secretaria(FuncionarioAssalariado):
    def trabalhar(self, horas):
        print(f"{self.nome} passa {horas} horas arrumando a papelada.")

class Vendedor(FuncionarioComissionado):
    def trabalhar(self, horas):
        print(f"{self.nome} passa {horas} horas no telefone.")


class TrabalhadorFabrica(FuncionarioPagoPorHora):
    def trabalhar(self, horas):
        print(f"{self.nome} fabrica bugigangas por {horas} horas.")


# HERANÇA MÚLTIPLA
class SecretariaTemporaria(Secretaria, FuncionarioPagoPorHora):
    def __init__(self, id, nome, horas_trabalhadas, ganho_por_hora):
        FuncionarioPagoPorHora.__init__(self,id,nome,horas_trabalhadas,ganho_por_hora)
    
    def calcular_folha(self):
        return FuncionarioPagoPorHora.calcular_folha(self)