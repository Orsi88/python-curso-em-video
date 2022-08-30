#from math import fabs

lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))

#if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2 and lado1 == lado2 and lado2 == lado3:
    #print('Os lados {}, {} e {} formam um triângulo equilátero!'.format(lado1, lado2, lado3))
#elif lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2 and lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
   # print('Os lados {}, {} e {} formam um triângulo isóceles!'.format(lado1, lado2, lado3))
#elif lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2 and lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    #print('Os lados {}, {} e {} formam um triângulo escaleno!'.format(lado1, lado2, lado3))
#else:
    #print('Os lados {}, {} e {} NÃO podem formar um triângulo!'.format(lado1, lado2, lado3))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os lados {}, {} e {} formam um triângulo!'.format(lado1, lado2, lado3))
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO!')
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')
