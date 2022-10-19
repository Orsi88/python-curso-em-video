# Calculadora simples

escolha = ''
valor1 = 0
valor2 = 0
resultado = 0

# Recebendo info
def recebendoInfo():
    valor1 = float(input('Digite um número: '))
    valor2 = float(input('Digite outro número: '))
    
    return valor1 and valor2
# Criando Menu

def manipulandoQuestão():
    print('-=-'*15)
    print('[1] Somar')
    print('[2] Mutiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    print('-=-'*15)

    escolha = input('Você deseja realizar qual operação? ')
    return escolha

# Testando
while escolha != '5':
    recebendoInfo()
    manipulandoQuestão()
    if escolha == '1':
        resultado = valor1 + valor2
    elif escolha == '2':
        resultado = valor1 * valor2
        print(resultado)
    elif escolha == '3':
        if valor1 > valor2:
            resultado = valor1
            print(resultado)
        elif valor2 > valor1:
            resultado = valor2
            print(resultado)
        elif valor1 == valor2:
            resultado = 'Os vaores são iguais'
            print(resultado)
    elif escolha == '4':
        recebendoInfo()
        manipulandoQuestão()
    elif escolha == '5':
        break
    