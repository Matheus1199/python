s = int(input('Qual é o salário do funcionário? '))
if s < 5000:
    s2 = s + s * 0.15
else:
    s2 = s + s * 0.10
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s, s2))