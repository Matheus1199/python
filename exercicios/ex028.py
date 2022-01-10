import random

print('Você vai ter que adivinhar que número eu estou pensando!')
n = int(input('Qual número você acha é (entre 0 e 5)?  '))
r = str(random.randint(0, 5))
if n == r:
    print('Você acertou PARABÉNS!')
else:
    print('Você errou, tente novamente!')
