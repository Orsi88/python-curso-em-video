from datetime import date

nomedoJovem = str(input('Digite seu nome: '))
sexodoJovem = str(input('Qual o seu sexo [f/m]? '))
anodeNascimentodoJovem = int(input('Digite o ano que você nasceu: '))

ano = date.today().year
idadedoJovem = ano - anodeNascimentodoJovem

if 18 == idadedoJovem and sexodoJovem == 'm':
    print(nomedoJovem,', já é hora de se alistar!!')
elif 18 < idadedoJovem and sexodoJovem == 'm':
    print(nomedoJovem,', já passou da hora de se alistar!!')
    anosAtraso = idadedoJovem - 18
    print('Passou {} anos do prazo de alistamento!!'.format(anosAtraso))
elif 18 > idadedoJovem and sexodoJovem == 'm':
    print(nomedoJovem,', você ainda vai se alistar!!')
    anosFalta = 18 - idadedoJovem
    print('Faltam {} anos para você se alistar!'.format(anosFalta))
else:
    print(nomedoJovem,', você não precisa se alistar! ')


