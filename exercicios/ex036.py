print('-=-'*20)
print('Calculo de empréstimo bancário')
print('-=-'*20)

preco = float(input('Digite o valor do imóvel: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite quantos anos vai demorar para pagar: '))

prestacao = preco/(anos * 12)
print('O valor da prestção mensal é de R${:.2f}'.format(prestacao))

if prestacao > (salario * 0.3):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')
