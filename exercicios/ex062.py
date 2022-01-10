print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(primeiro), end='')
        cont += 1
        primeiro += razao
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))    
print('Progressão finalizada com {} termos mostrados.'.format(total))
