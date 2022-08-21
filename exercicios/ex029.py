#velocidade = float(input('Digite a sua velocidade [Km/h]: '))

#if(velocidade > 80):
    #print('MULTADO!')
    #multa = (velocidade - 80) * 7
    #print('Você deverá pagar o valor de R${} por ter ultrapassado o limete de velocidade do local.'.format(multa))
#else:
   #print('Tá tranquilo!')

velocidade = float(input('Qual é a velocidade atial do carro [Km]? '))

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! DIrija com segurança!')
