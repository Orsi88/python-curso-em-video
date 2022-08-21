from posixpath import split


cidade = input('Digite o nome da sua cidade: ')
#cidade = str(input('Digite o nome da sua cidade: ')).strip()
nomeCidade = cidade.split()

print(nomeCidade[0] == 'Santo')
#print(cidade[:5].upper() == 'SANTO') 