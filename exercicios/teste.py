nome = input('Digite seu nome completo: ')

primeiroNome = nome.split()
letrasNome = len(primeiroNome[0])

print('O seu primeiro nome é {}'.format(primeiroNome[0]))
print('A quantidade de letras do seu primeiro nome é {}'.format(letrasNome))