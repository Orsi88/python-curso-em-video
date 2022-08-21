celsius = float(input('Digite aqui a temperatura em °C que deseja converter para °F: '))

f = (celsius * 1.8) + 32

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(celsius, f))