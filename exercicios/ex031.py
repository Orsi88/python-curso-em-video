distancia = float(input('Qual é a distância entre o local de partida e o local de chegada [Km]? '))

if(distancia <= 200):
    passagem = (distancia * 0.50)
else:
    passagem = (distancia * 0.45)
    
print('O valor da passagem é de R${}'.format(passagem))
print('FIM!')