nome = input('Digite seu nome completo: ')

quantidadeLetras = nome.replace(" ", "")
semEspaco = nome.split()

print(nome.upper())
print(nome.lower())
print('O seu nome possui {} letras!'.format(len(quantidadeLetras)))
print('O seu primeiro nome possui {} letras!'.format(len(semEspaco[0])))