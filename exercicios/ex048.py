soma = 0
for n in range(1, 500):
    if n% 3 == 0:
        print(n)
        soma += n
print('A soma dos valores é: {}'.format(soma))
print('FIM')