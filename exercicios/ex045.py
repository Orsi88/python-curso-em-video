#🖐
#👊
#✌
#⏳
#🕗
#⚔️
#👏
#💔
#🏆
#💻
#😘

#cronomêtro
#from time import sleep
#import os
#for c in range(10, 0, -1):
    #print(c)
    #sleep(1)
    #os.system('cls')
#print('FIM')

#iniciando jogo
from time import sleep
from random import randint
import os

print('*'*20)
print('       JOKENPÔ       ')
print('*'*20)
print('\n  Você  ⚔️   Máquina  \n')

print('Rodada 1/3')

print('[1] 👊 - pedra')
print('[2] 🖐 - papel')
print('[3] ✌ - tesoura')

jogadaHumano = str(input('Sua vez: '))
jogadaMaquina = randint(1, 3)

for c in range(3, 0, -1):
    os.system('cls')
    print('_'*10,c,'_'*10)
    sleep(1)
    os.system('cls')

if jogadaHumano == '1':
    print('Humano:👊')
elif jogadaHumano == '2':
    print('Humano:🖐')
elif jogadaHumano == '3':
    print('Humano:✌')

if jogadaMaquina == '1':
    print('Máquina:👊')
elif jogadaMaquina == '2':
    print('Máquina:🖐')
elif jogadaMaquina == '3':
    print('Máquina:✌')





