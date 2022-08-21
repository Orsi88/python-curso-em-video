from unittest import result


y = int(input('Digite o número que deseja saber a sua tabuada: '))

cont = 0


while(cont <= 10):
    resposta = y * cont
    print('{} x {} = {}'.format(y, cont, resposta))
    cont = cont + 1
