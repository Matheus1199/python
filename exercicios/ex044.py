print('='*10, 'Lojas Barsotti', '='*10)
preco = float(input('Preço da compra: R$'))
print('''Qual é a forma de pagamento:
[ 1 ] à vista dinherio/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    total = preco + (preco * 20 / 100)
    precoParcela = total / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, precoParcela)) 
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, total))