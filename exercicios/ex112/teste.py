from utilidades import moeda
from utilidades import dado

p = dado.leiaDinheiro('Digite o preço: R$')
t = int(input('Qual o valor da taxa? '))
moeda.resumo(p, t)
