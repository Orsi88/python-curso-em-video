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
import random
import os

pontoHumano = 0
pontoMaquina = 0
cont = 1

while cont <= 3:

    os.system('cls')

    print('*'*20)
    print('       JOKENPÔ       ')
    print('*'*20)
    print('\n  Você  ⚔️   Máquina  \n')

    print('Rodada {}/3'.format(cont))

    print('[a] 👊  - pedra')
    print('[b] 🖐  - papel')
    print('[c] ✌  - tesoura')

    a = '👊'
    b = '🖐'
    c = '✌'

    jogadas = [a, b, c]
    jogadaHumano = str(input('Sua vez: '))

    if jogadaHumano == 'a':
        jogadaHumano = '👊'
    elif jogadaHumano == 'b':
        jogadaHumano = '🖐'
    elif jogadaHumano == 'c':
        jogadaHumano = '✌'

    jogadaMaquina = random.choice(jogadas)

    for c in range(3, 0, -1):
        os.system('cls')
        print('⏳   ', c, '   ⏳')
        sleep(1)
        os.system('cls')
    print('JO  -  KEN  -  PÔ \n')
    print(jogadaHumano, '     ⚔️     ', jogadaMaquina)

    if jogadaHumano == '👊' and jogadaMaquina == '👊':
        print('\nRodada empatada')
        cont = cont + 0
    elif jogadaHumano == '🖐' and jogadaMaquina == '🖐':
        print('\nRodada empatada')
        cont = cont + 0
    elif jogadaHumano == '✌' and jogadaMaquina == '✌':
        print('\nRodada empatada')
        cont = cont + 0
    elif jogadaHumano == '🖐' and jogadaMaquina == '👊':
        pontoHumano = pontoHumano + 1
        print('\nVocê venceu a rodada {}/3 👏'.format(cont))
        cont = cont +1
    elif jogadaHumano == '✌' and jogadaMaquina == '🖐':
        pontoHumano = pontoHumano + 1
        print('\nVocê venceu a rodada {}/3 👏'.format(cont))
        cont = cont +1
    elif jogadaHumano == '👊' and jogadaMaquina == '✌':
        pontoHumano = pontoHumano + 1
        print('\nVocê venceu a rodada {}/3 👏'.format(cont))
        cont = cont +1
    elif jogadaHumano == '👊' and jogadaMaquina == '🖐':
        pontoMaquina = pontoMaquina + 1
        print('\nA máquina venceu a rodada {}/3😘'.format(cont))
        cont = cont +1
    elif jogadaHumano == '🖐' and jogadaMaquina == '✌':
        pontoMaquina = pontoMaquina + 1
        print('\nA máquina venceu a rodada {}/3😘'.format(cont))
        cont = cont +1
    elif jogadaHumano == '✌' and jogadaMaquina == '👊':
        pontoMaquina = pontoMaquina + 1
        print('\nA máquina venceu a rodada {}/3😘'.format(cont))
        cont = cont +1

    #a > b  and c > b and a > c  
    sleep(3)


print('*'*20)
print('       JOKENPÔ       ')
print('*'*20)

if pontoHumano > pontoMaquina:
    print('Parabéns, você veceu a Partida!!')
    print('🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆')
else:
    print('A máquina venceu a Partida!!')
    print('💔💔💔💔💔💔💔💔')





