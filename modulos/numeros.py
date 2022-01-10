from uteis import numeros as n

# Programa Principal
num = int(input('Digite um valor: '))
fat = n.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {n.dobro(num)}')
print(f'O triplo de {num} é {n.triplo(num)}')
