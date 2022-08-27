primeiroValor = int(input('Digite o priemiro valor: '))
segundoValor = int(input('Digite o segundo valor: '))

if primeiroValor == segundoValor:
    print('Os valores são iguais!')
elif primeiroValor > segundoValor:
    print('O número {} é maior!'.format(primeiroValor))
elif primeiroValor < segundoValor:
    print('O número {} é maior!'.format(segundoValor))