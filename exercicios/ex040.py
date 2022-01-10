n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media > 7:
    print('Sua média foi de {}, você está APROVADO!'.format(media))
elif media >= 5 and media < 6.9:
    print('Sua média foi de {}, você está de RECUPERAÇÃO!'.format(media))
else:
    print('Sua média foi de {}, você está REPROVADO!'.format(media))