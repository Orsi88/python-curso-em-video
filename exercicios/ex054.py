soma = 0
for cont in range(1, 8):
    nome = str(input('Digite o seu nome: '))
    idade = int(input('DIgite a sua idade: '))
    if idade < 21:
        anosFalta = 21 - idade
        print('{}, você é de menor! O total de anos até a sua maioridade é de: {}'.format(nome, anosFalta))
    else:
        print('{}, é de maior'.format(nome))
        soma = soma + 1
print('Dentre as sete pessoas analisadas {} estão dentro da maioridade!'.format(soma))
