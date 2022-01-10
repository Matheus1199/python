valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valorcasa / (anos * 12)
if prestacao <= salario * 0.3:
    print('O valor da casa é de R${:.2f}, o seu salário é de R${:.2f} e a prestação será de R${:.2f}, seu empréstimo foi CONCEDIDO!'.format(valorcasa, salario, prestacao))
else:
    print('O valor da casa é de R${:.2f}, o seu salário é de R${:.2f} e a prestação será de R${:.2f}, seu empréstimo foi NEGADO!'.format(valorcasa, salario, prestacao))