def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param: f: fim da contagem
    :param: p: passo da contagem
    :return: sem retorno
    Função criada por Matheus Bonafin
    """
    while i <= f:
        print(f'{i}', end='')
        i += p
    print('FIM')

help(contador)