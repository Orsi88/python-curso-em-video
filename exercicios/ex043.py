peso = float(input('Digite seu peso [Kg]: '))
altura = float(input('Digite sua altura [m]: '))

imc = peso/(altura**2)
print('Seu imc está em: {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc > 18.5 and imc < 25:
    print('Você está no seu Peso ideal!')
elif imc > 25 and imc < 30:
    print('Você está com sobrepeso!')
elif imc > 30 and imc < 40:
    print('Você está com obesidade!')
elif imc > 40:
    print('Você está com obesidade mórbida!')