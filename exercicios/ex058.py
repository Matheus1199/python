import random

print('Sou o seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
n = int(input('Qual é o seu palpite? '))
r = int(random.randint(0, 10))
palpites = 0
while n != r:
    if n < r:
        print('Mais... Tente mais uma vez.')
        palpites += 1
    elif n > r:
        print('Menos... Tente mais uma vez.')
        palpites += 1
    n = int(input('Qual é o seu palpite? '))
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
        