altura = float(input('Digite a Altura da parede em metros: '))
largura = float(input('Digite a Largura da parede em metros:'))

area = altura * largura
quantTinta = area / 2

print('A área da sua parede é de {} m², serão necessárias {} latas de tinta!'.format(area, quantTinta))