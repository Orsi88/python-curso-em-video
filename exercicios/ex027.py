nome = input('Digite seu nome completo: ')

nomeCompleto = nome.split()
primeiroNome = nomeCompleto[0]
ultimoNome = nomeCompleto[-1]


print('Primeiro nome: {}'.format(primeiroNome))
print('Último nome: {}'.format(ultimoNome))