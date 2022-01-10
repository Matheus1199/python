v = float(input('Qual a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite pertimido que é 80km/h')
    m = (v - 80) * 7
    print('Você deve pagar um multa de {:.2f}'.format(m))
    print('Você terá que pagar {}')
print('Tenha um bom dia! Dirija com segurança!')
