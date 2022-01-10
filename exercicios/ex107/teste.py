import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
t = int(input('Qual o valor da taxa? '))
print(f'Aumentando {t}%, temos R${moeda.aumentar(p, t)}')
print(f'Diminuindo {t}%, temos R${moeda.diminuir(p, t)}')
