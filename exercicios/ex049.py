n = int(input('Digite o número que deseja saer a tabuada: '))

for cont in range(0, 11):
    m = n * cont
    print('{} x {} = {}'.format(n, cont, m))
