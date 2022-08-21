from math import fabs

lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terciero lado: '))

if(lado2 + lado3) > lado1 > fabs(lado2 - lado3) or (lado1 + lado3) > lado2 > fabs(lado1 - lado3) or (lado1 + lado2) > lado3 > fabs(lado1 - lado2):

#if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:

    print('Os lados {}, {} e {} podem SIM formar um triângulo!'.format(lado1, lado2, lado3))
else:
    print('Os lados {}, {} e {} NÃO podem formar um triângulo!'.format(lado1, lado2, lado3))

