km = float(input('Qual a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km.')
if km < 200:
    print('Você deverá pagar R${}'.format(km * 0.5))
else:
    print('Você deverá pagar R${}'.format(km * 0.45))