def notas(*n, sit=False):
    """
    -> Função para analisar as notas e situação de um aluno.
    :param n: uma ou mais notas do aluno (aceita várias).
    :param sit: (valor opcional), indicando se deve ou não aceitar a situação.
    :return: dicionário com várias informações sobre as notas do aluno.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 9:
            r['situacao'] = 'EXCELENTE'
        elif r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

