import moeda

p = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
t = int(input('Qual o valor da taxa? '))
print(f'Aumentando {t}%, temos {moeda.moeda(moeda.aumentar(p, t))}')
print(f'Diminuindo {t}%, temos {moeda.moeda(moeda.diminuir(p, t))}')
