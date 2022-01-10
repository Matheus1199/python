from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 20 )
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)    
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valore ao todo.')
    print(f'O maior valor informado foi {maior}')

# Programa Principal
maior(2, 6, 5, 9, 8, 4)
maior(1, 8, 4)
maior(1, 2)
maior(8)
maior()