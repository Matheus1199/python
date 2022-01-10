def aumentar(preco=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento ou redução
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato
    '''
    res = preco + (preco * taxa / 100)
    return res if format is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if format is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if format is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco - preco / 2
    return res if format is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxa=0, formato=False):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'{taxa}% de redução: \t{diminuir(preco, taxa, True)}')
    print('-' * 30)
