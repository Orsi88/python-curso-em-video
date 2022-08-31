#n = int(input('Digite um número e descubra se ele é primo ou não: '))

#if n % 2 == 0:
    #print('Não é primo')
#elif n % 3 == 0:
    #print('Não é primo')
#elif n % 5 == 0:
    #print('Não é primo')
#elif n % 7 == 0:
    #print('Não é primo')
#else:
    #print('É primo')

primo = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print(' {} '.format(c))
        primo += 1

if primo == 2:
    print('O número {} é PRIMO'.format(num))
else:
    print('O número {} NÃO é PRIMO'.format(num))

