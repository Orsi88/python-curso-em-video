dias = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram percorridos? '))

apagar = (60 * dias) + (km * 0.15)

print('O total a pagar é de R${}'.format(apagar))
