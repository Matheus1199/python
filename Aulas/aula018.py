teste = list()
teste.append('Matheus')
teste.append(16)
galera = list()
galera.append(teste[:])
teste[0] = 'Lucas'
teste[1] = 17
galera.append(teste[:])
print(galera)