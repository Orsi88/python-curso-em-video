from importlib import import_module
import math


import random

g1 = input('Digite o nome do lider do grupo 1: ')
g2 = input('Digite o nome do lider do grupo 2: ')
g3 = input('Digite o nome do lider do grupo 3: ')
g4 = input('Digite o nome do lider do grupo 4: ')

grupos = [g1, g2, g3, g4]
sorteio = random.sample(grupos, len(grupos))

print('A ordem sorteada foi: \n{}'.format(sorteio))