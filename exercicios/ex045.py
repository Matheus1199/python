from random import randint
import time

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
time.sleep(2)
print('KEN')
time.sleep(2)
print('PO!!!')
print('-=' * 11)
print('O Jogador escolheu {}'.format(itens[jogador]))
print('O Computador escolheu {}'.format(itens[computador]))
print('-=' * 11)
if computador == 0: #Computador jogou pedra
    if jogador == 0: #jogador jogou pedra
        print('EMPATE')
    
    elif jogador == 1: #jogador jogou papel
        print('JOGADOR VENCEU')
    
    elif jogador == 2: #jogador jogou tesoura
        print('COMPUTADOR VENCEU')
    
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #computador jogou papel
    if jogador == 0: #jogador jogou pedra
        print('COMPUTADOR VENCEU')
    
    elif jogador == 1: #jogador jogou papel
        print('EMPATE')
    
    elif jogador == 2: #jogador jogou tesoura
        print('JOGADOR VENCEU')
    
    else:
        print('JOGADA INVÁLIDA')
        

elif computador == 2: #computador jogou tesoura
    if jogador == 0: #jogador jogou pedra
        print('JOGADOR VENCEU')
    
    elif jogador == 1: #jogador jogou papel
        print('COMPUTADOR VENCE')
    
    elif jogador == 2: #jogador jogou tesoura
        print('EMPATE')
    
    else:
        print('JOGADA INVÁLIDA')
        


