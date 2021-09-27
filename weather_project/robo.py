from time import sleep
from temperatura import obtem_temperatura

local = input('Digite o local (ex.: Estado, País): ')

temp_atual = obtem_temperatura(local)

print("Eu sou um Robo!")
print("Temperatura atual:",temp_atual['temp'])
print("Temperatura maxima:",temp_atual['temp_max'])
print("Temperatura minima:",temp_atual['temp_min'])

if temp_atual['temp'] < 20:
    print("Tá frio! É melhor você pegar um casaco!")
elif temp_atual['temp'] > 27:
    print('Ta tão quente, que da até pra estralar um ovo no asfalto!')
else :
   print('Hoje está bem de boa a temperatura')

sleep(10)
