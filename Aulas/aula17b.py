valores = []
for cont in range(0, 6):
    valores.append(int(input('Digite u valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')