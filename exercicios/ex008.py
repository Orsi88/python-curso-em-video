x = float(input('Digite um valor em metros: '))

km = x * 10 ** -3
hm = x * 10 ** -2
dam = x * 10 ** -1
dm = x * 10 ** 1
cm = x * 10 ** 2
mm = x * 10 ** 3

print('O valor {} m, é igual a:'.format(x))
print('{} km \n{} hm \n{} dam \n{} dem \n{} cm \n{} mm'.format(km, hm, dam, dm, cm, mm))