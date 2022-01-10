from datetime import date

nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))

else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))