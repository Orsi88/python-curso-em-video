from random import randint
from time import sleep

cont = 0
computador = randint(0, 5)
jogador = 9999

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

while jogador != computador:
    jogador = int(input('Em que número pensei? '))
    print('PROCESSANDO...')
    sleep(3)
    if jogador != computador:
        print('\nErrou!\n')
    cont += 1

print('Acertou!')
print('Foram executadas {} tentativas'.format(cont)) 
