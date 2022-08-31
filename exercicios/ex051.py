a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))

for n in range(1 , 11): 
    a = a1 + (n - 1) * r
    print('O valor de a{} é {}'.format(n, a))