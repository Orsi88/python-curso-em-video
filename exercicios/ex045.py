#π
#π
#β
#β³
#π
#βοΈ
#π
#π
#π
#π»
#π

#cronomΓͺtro
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
    print('       JOKENPΓ       ')
    print('*'*20)
    print('\n  VocΓͺ  βοΈ   MΓ‘quina  \n')

    print('Rodada {}/3'.format(cont))

    print('[a] π  - pedra')
    print('[b] π  - papel')
    print('[c] β  - tesoura')

    a = 'π'
    b = 'π'
    c = 'β'

    jogadas = [a, b, c]
    jogadaHumano = str(input('Sua vez: '))

    if jogadaHumano == 'a':
        jogadaHumano = 'π'
    elif jogadaHumano == 'b':
        jogadaHumano = 'π'
    elif jogadaHumano == 'c':
        jogadaHumano = 'β'

    jogadaMaquina = random.choice(jogadas)

    for c in range(3, 0, -1):
        os.system('cls')
        print('β³   ', c, '   β³')
        sleep(1)
        os.system('cls')
    print('JO  -  KEN  -  PΓ \n')
    print(jogadaHumano, '     βοΈ     ', jogadaMaquina)

    if jogadaHumano == 'π' and jogadaMaquina == 'π':
        print('\nRodada empatada')
        cont = cont + 0
    elif jogadaHumano == 'π' and jogadaMaquina == 'π':
        print('\nRodada empatada')
        cont = cont + 0
    elif jogadaHumano == 'β' and jogadaMaquina == 'β':
        print('\nRodada empatada')
        cont = cont + 0
    elif jogadaHumano == 'π' and jogadaMaquina == 'π':
        pontoHumano = pontoHumano + 1
        print('\nVocΓͺ venceu a rodada {}/3 π'.format(cont))
        cont = cont +1
    elif jogadaHumano == 'β' and jogadaMaquina == 'π':
        pontoHumano = pontoHumano + 1
        print('\nVocΓͺ venceu a rodada {}/3 π'.format(cont))
        cont = cont +1
    elif jogadaHumano == 'π' and jogadaMaquina == 'β':
        pontoHumano = pontoHumano + 1
        print('\nVocΓͺ venceu a rodada {}/3 π'.format(cont))
        cont = cont +1
    elif jogadaHumano == 'π' and jogadaMaquina == 'π':
        pontoMaquina = pontoMaquina + 1
        print('\nA mΓ‘quina venceu a rodada {}/3π'.format(cont))
        cont = cont +1
    elif jogadaHumano == 'π' and jogadaMaquina == 'β':
        pontoMaquina = pontoMaquina + 1
        print('\nA mΓ‘quina venceu a rodada {}/3π'.format(cont))
        cont = cont +1
    elif jogadaHumano == 'β' and jogadaMaquina == 'π':
        pontoMaquina = pontoMaquina + 1
        print('\nA mΓ‘quina venceu a rodada {}/3π'.format(cont))
        cont = cont +1

    #a > b  and c > b and a > c  
    sleep(3)


print('*'*20)
print('       JOKENPΓ       ')
print('*'*20)

if pontoHumano > pontoMaquina:
    print('ParabΓ©ns, vocΓͺ veceu a Partida!!')
    print('ππππππππππππππ')
else:
    print('A mΓ‘quina venceu a Partida!!')
    print('ππππππππ')





