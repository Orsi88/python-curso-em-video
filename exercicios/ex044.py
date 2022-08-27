valoraPagar = float(input('Digite o valor a ser pago: R$ '))
print('-=-'*20)
print('[1] Dinheiro com 10% de desconto')
print('[2] Á vista no cartão com 5% de desconto')
print('[3] Até 2x no cartão')
print('[4] Acima de 3x no cartão com 20% de juros')
print('-=-'*20)
formadePagamento = str(input('Escolha a forma de pagamento: '))

if formadePagamento == '1':
    valorAtualizado = valoraPagar - (valoraPagar * 0.1)
    print('Pague R${}'.format(valorAtualizado))
elif formadePagamento == '2':
    valorAtualizado = valoraPagar - (valoraPagar * 0.05)
    print('Pague R${}'.format(valorAtualizado))
elif formadePagamento == '3':
    print('Pague R${}'.format(valoraPagar))
elif formadePagamento == '4':
    valorAtualizado = valoraPagar + (valoraPagar * 0.2)
    print('Pague R${}'.format(valorAtualizado))

print('Agradecemos por comprar conosco, volte sempre!')


