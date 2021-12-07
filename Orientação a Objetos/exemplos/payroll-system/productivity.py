class SistemaProdutividade():
    def monitorar(self, funcionarios, horas):
        print("Monitorando a produtividade dos funcionarios")
        print("============================================")
        for funcionario in funcionarios:
            funcionario.trabalhar(horas)
        print('')