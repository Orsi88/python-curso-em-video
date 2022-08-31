idadeHomemMaisVelho = 0
mulheres = 0 
soma = 0

for grupo in range(1, 5):
    print('----{}° PESSOA----'.format(grupo))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo =  str(input('Digite seu sexo [f/m]: '))

    soma = soma + idade
    if sexo == 'm' and idade > idadeHomemMaisVelho:
        homemMaisVelho = nome
        idadeHomemMaisVelho = idade
    if sexo == 'f' and idade < 20 :
        mulheres = mulheres + 1

media = soma/4

print('A média das idade é {}'.format(media))
print('O homem mais velho é {}'.format(homemMaisVelho))
print('A quantidade de mulheres com menos de 20 anos é de {}'.format(mulheres))