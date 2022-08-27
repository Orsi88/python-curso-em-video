nota1 = float(input('Digite a sua nota na primeira prova: '))
nota2 = float(input('Digite a sua nota na sengunda prova: '))

media = (nota1 + nota2)/2

if media >= 7:
    print('APROVADO')
elif media > 5 and media < 6.9:
    print('RECUPERAÇÃO')
elif media < 5:
    print('REPROVADO')

