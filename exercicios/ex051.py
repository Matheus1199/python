primeiro =int(input('Primeiro termo: '))
razao = int(input('Raz�o: '))
decimo = primeiro + (11 - 1) * razao
for c in range(primeiro, decimo, razao):
    print('{} '.format(c), end=' ')
print('ACABOU!')
