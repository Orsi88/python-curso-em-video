from datetime import date

anodeNascimentodoAtleta = int(input('Digite o seu ano de nascimento: '))

ano = date.today().year
idade = ano - anodeNascimentodoAtleta

if idade <= 9:
    print('Você tem {} anos, logo é um atleta: '.format(idade))
    print('MIRIM')
elif idade <= 14:
    print('Você tem {} anos, logo é um atleta: '.format(idade))
    print('INFANTIL')
elif idade <= 19:
    print('Você tem {} anos, logo é um atleta: '.format(idade))
    print('JUNIOR')
elif idade <= 20:
    print('Você tem {} anos, logo é um atleta: '.format(idade))
    print('SÊNIOR')
elif idade > 20:
    print('Você tem {} anos, logo é um atleta: '.format(idade))
    print('MASTER')
