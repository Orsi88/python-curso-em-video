#import math

#import random

#numeroSorteado = random.randrange(0, 5, 1)
#numeroEscolhido = int(input('Digite um número entre 0 e 5 e veja se acertou o número sorteado: '))

#if(numeroEscolhido == numeroSorteado):
    #print('Parabéns, você acertou!')
#else:
    #print('Você errou! O computador venceu!')

#print('FIM')



from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)

if(jogador == computador):
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
