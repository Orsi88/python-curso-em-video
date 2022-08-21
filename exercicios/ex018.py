from math import sin, cos, tan, radians


angulo = float(input('Digite o valor do ângulo: '))

sen = sin(radians(angulo))
coss = cos(radians(angulo))
tag = tan(radians(angulo))

print('O seno do ângulo {} é igual a {:.2f} \nO cosseno do ângulo {} é igual a {:.2f} \nA tangente do ângulo {} é igual a {:.2f}'.format(angulo, sen, angulo, coss, angulo, tag))