class Cubo:
    """Cria, calcula e retorna o cubo de um número"""
    def __init__(self, numero):
        self.numero = numero
        print(f"Objeto criado! (Passado arg. numero com valor {self.numero})")
    
    def calcular_cubo(self):
        return f"Cubo calculado: {self.numero ** 3}"

el = Cubo(6)
print(el.calcular_cubo())
        