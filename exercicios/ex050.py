s = 0
c = 0
for cont in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        c += 1
        s += n
        
print('A soma do números pares digitados é: {}'.format(s))
print('A quantidade de números pares digitados é: {}'.format(c))