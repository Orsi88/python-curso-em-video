x = input('Digite algo: ')
print('O tipo primitivo desse vaor é ',type(x)) #ele devolve o tipo do input.
print('Só tem espaço? ', x.isspace()) #o comando .isspace se refere aos espaços, se houver apenas espaços ele recebe o valor de True se houver algo além de espaços ele recebe o valor False.
print('É um número? ', x.isnumeric()) #ele vai detectar se o valor inserido é um número, msm se o tipo for string ele vai saber diferenciar se é um número ou outra coisa.
print('É alfabético? ', x.isalpha()) # ele vai detectar se o valor é composto de letras.
print('É alfanumérico? ', x.isalnum()) #ele vai detectar se o valor inserido é alfanumérico, ou seja, se possui números e letras.
print('Está em maiúsculas? ', x.isupper()) #ele vai identificar se o valor está escrito em letras maiúsculas.
print('Está em minúsculas? ', x.islower()) #ele vai identificar se o valor está escrito em letras minúsculas.
print('Está capitalizada? ', x.istitle()) #ele vai identificar se o valor tem a primeira letra em maiúsculo e o restante em minúsculo.