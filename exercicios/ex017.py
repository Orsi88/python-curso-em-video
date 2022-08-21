from math import hypot


co = float(input('Digite o valor do cateto oposto em cm: '))
ca = float(input('Digite o valor do cateto adjacente em cm: '))

hip = hypot(co, ca)

print('O comprimento da hipotenusa é {} cm'.format(hip))