salario = float(input('Quanto é o seu salário? '))

if(salario > 1250):
    reajuste = salario + (salario * 0.10)
    print('O seu salário agora com o reajuste será de R${}!'.format(reajuste))
else:
    reajuste = salario + (salario * 0.15)
    print('O seu salário agora com o reajuste será de R${}!'.format(reajuste))
print('FIM')
