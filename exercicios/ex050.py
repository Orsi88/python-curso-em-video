s = 0
for cont in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print('A soma do números pares digitados é: {}'.format(s))
