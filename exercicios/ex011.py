largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = altura * largura
pintura = altura * largura / 2
print('A área da parede é de {}'.format(area))
print('Para pintar essa parede será necessário {} litros de tinta'.format(pintura))

