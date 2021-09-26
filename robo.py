from time import sleep
from temperatura import obtem_temperatura

def robo_falante(nome, idade, cidade):
    print('Olá, eu sou um robô!')
    print('Eu sei que você se chama', nome)
    print('Possui', idade, 'anos')
    print('E mora na cidade de', cidade)

    temperatura_atual = obtem_temperatura(cidade)

    print('A temperatura atual é:', temperatura_atual)

robo_falante('Eduardo', 20,'São Paulo')

sleep(10)