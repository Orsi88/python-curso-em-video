pesos = []

for pessoas in range(1, 6):
    nome = str(input('Digite seu nome: '))
    peso = float(input('Digite o seu peso [Kg]: '))

    pesos.insert(pessoas, peso)
    print(pesos)

pesos.sort()
print(pesos)

print('O menor peso foi: {}'.format(min(pesos)))
print('O maior peso foi: {}'.format(max(pesos)))
    