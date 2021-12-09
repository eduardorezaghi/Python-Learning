class SistemaProdutividade():
    def monitorar(self, funcionarios, horas):
        print("Monitorando a produtividade dos funcionarios")
        print("============================================")
        for funcionario in funcionarios:
            funcionario.trabalhar(horas)
        print('')


class FuncaoGerencia:
    def trabalhar(self, horas):
        print(f"{self.nome} grita e xinga por {horas} horas.")


class FuncaoSecretaria:
    def trabalhar(self, horas):
        print(f"{self.nome} passa {horas} horas arrumando a papelada.")


class FuncaoVendas:
    def trabalhar(self, horas):
        print(f"{self.nome} passa {horas} horas no telefone.")


class FuncaoFabrica:
    def trabalhar(self, horas):
        print(f"{self.nome} fabrica bugigangas por {horas} horas.")