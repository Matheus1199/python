n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
soma = n1 + n2
multiplicar = n1 * n2
maior = 0
divisao = n1 / n2
while opcao != 7:
    print('''    [ 1 ] soma
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] divisão
    [ 6 ] Par ou impar
    [ 7 ] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print('A soma do {} e {} é igual a {}'.format(n1, n2, soma))
    elif opcao == 2:
        print('A multiplicação do {} e {} é igual a {}'.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            print('O número {} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que {}'.format(n2, n1))
        elif n1 == n2:
            print('Os números são iguais')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('A divisão do {} e {} é igual {}'.format(n1, n2, divisao))
    elif opcao == 6:
        if soma % 2 == 0:
            print('A soma dos números {} e {} é par'.format(n1, n2))
        else:
            print('A soma dos números {} e {} é ímpar'.format(n1, n2))
    elif opcao == 7:
        print('Finalizando...')
        print('Programa finalizado! Volte sempre!')
    else:
        print('Opção inválida! Tente novamente.')
print('Fim do programa! Volte sempre')
