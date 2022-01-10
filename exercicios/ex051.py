primeiro =int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (11 - 1) * razao
for c in range(primeiro, decimo, razao):
    print('{} '.format(c), end=' ')
print('ACABOU!')
