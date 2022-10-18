res = 0
while res == 0:
    sexo = input('Digite seu sexo [M/F]: ').upper()
    if sexo == 'M':
        print('Resposta salva.')
        res = 1
        break
    elif sexo == 'F':
        print('Resposta salva.')
        res = 1
        break
    else: 
        print('Resposta invalida! Tente novamente.')
        res = 0   