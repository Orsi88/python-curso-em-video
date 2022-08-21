salario = float(input('Qual o salário do funcionário? R$'))

reajuste = salario + (salario * 0.15)

print('O funcionário que ganhava R${}, com 15% de aumento, passa a receber R${}!'.format(salario, reajuste))