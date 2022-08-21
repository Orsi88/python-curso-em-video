precoVelho = float(input('Digite o preço do produto: '))

precoNovo = precoVelho - (precoVelho * 0.05)

print('O preço atualizado do produto com o desconto de 5% é R${:.2f}!'.format(precoNovo))