# Calculadora Simples

# Função para receber os valores

valor1 = float(input('Digite um número: '))
valor2 = float(input('Digite outro número: '))

# Manipulando valores
valores = []    
valores.insert(0, valor1)
valores.insert(0, valor2)

print(valores)

# Criação Menu

escolha = ''
resposta = 0

# Criação opções Menu

if escolha == '1':
    resposta = valor1 + valor2
elif escolha == '2':
    resposta = valor1 * valor2
elif escolha == '3':
    if valor1 > valor2:
        resposta = valor1
    elif valor1 < valor2:
        resposta = valor2


# Respetição Menu

while escolha != '5':
    