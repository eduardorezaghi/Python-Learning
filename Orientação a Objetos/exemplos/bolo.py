from time import sleep
from datetime import datetime

class Bolo():
    cozinheiro = 'Godoi'

    def __init__(self, sabor,
                 tempera_de_aquecimento, tempo_de_aquecimento,
                 tempera_de_assadura, tempo_de_assadura,
                 tipo_do_forno = 'industrial'):
        self.sabor = sabor
        self.tempera_de_aquecimento = tempera_de_aquecimento
        self.tempo_de_aquecimento = tempo_de_aquecimento
        self.tempera_de_assadura = tempera_de_assadura
        self.tempo_de_assadura = tempo_de_assadura
        self.tipo_do_forno = tipo_do_forno

    def anuncio_inicio(self, dia):
        return f"""--- ({dia})
    O bolo de ({self.sabor}):"""

    def preparacao(self):
        return f"""    O forno ({self.tipo_do_forno}) esta pré-aquecendo a "{self.tempera_de_aquecimento}º" graus celsius, por ({self.tempo_de_aquecimento} minutos)"""

    def cozimento(self):
        return f"""    foi a forno á "{self.tempera_de_assadura}º" graus celsius, por ({self.tempo_de_assadura} minutos), pelo cozinheiro ({self.cozinheiro})..."""

    def anuncio_finalizacao(self):
        return f"O bolo de ({self.sabor}): foi pronto depois de {self.tempo_de_aquecimento + self.tempo_de_assadura} pelo forno ({self.tipo_do_forno})!"

    def faz_bolo(self):
        # imprime sobre anuncio inicial
        dia = datetime.now().isoformat()
        mensagem_anuncio_inicio = self.anuncio_inicio(dia=dia)
        print(mensagem_anuncio_inicio)
        # imprime sobre preparacao
        print(self.preparacao())
        # imprime sobre cozimento
        print(self.cozimento())
        # dorme por 3 segundos
        sleep(3)
        # imprime sobre finalização
        print(self.anuncio_finalizacao())


bolo_de_laranja = Bolo(sabor='Laranja',
                       tempera_de_aquecimento=100,
                       tempo_de_aquecimento=20,
                       tempera_de_assadura=180,
                       tempo_de_assadura=40,
                       tipo_do_forno='industrial')
bolo_de_laranja.faz_bolo()


bolo_de_coco = Bolo(sabor='Coco',
                    tempo_de_aquecimento=40,
                    tempera_de_aquecimento=200,
                    tempo_de_assadura=40,
                    tempera_de_assadura=250,
                    tipo_do_forno='caseiro')
bolo_de_coco.faz_bolo()

bolo_prestigio = Bolo(sabor='Prestigio',
                      tempo_de_aquecimento=20,
                      tempera_de_aquecimento=80,
                      tempo_de_assadura=40,
                      tempera_de_assadura=120,
                      tipo_do_forno='industrial')
bolo_prestigio.faz_bolo()
