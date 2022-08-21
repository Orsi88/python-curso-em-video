frase = str(input('Digite qualquer coisa: ')).upper().strip()

print('A letra a aparece {} vezes na sua frase!'.format(frase.count('A')))
print('A posição do primeiro a é: {}'.format(frase.find('A')+1))
print('A posição do último a é: {}'.format(frase.rfind('A')+1))