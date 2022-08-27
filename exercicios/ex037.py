numeroInteiro = int(input('Digite qualquer número inteiro: '))
print('-=-'*20)
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
print('-=-'*20)
baseDeConversão = str(input('Qual será a base de conversão? '))

if baseDeConversão == '1':
    bina = str(bin(numeroInteiro))
    print(bina)
elif baseDeConversão == '2':
    octa = str(oct(numeroInteiro))
    print(octa)
elif baseDeConversão == '3':
    exa = str(hex(numeroInteiro))
    print(exa)
else:
    print('Opção invalida!')


