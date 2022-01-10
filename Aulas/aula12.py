nome = str(input('Qual é o seu nome? '))
if nome == 'Isabela' or nome == 'Humberto':
    print('Que nome feio!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Juliana Jéssica':
    print('Belo nome feminino')
else:
    print('Seu nome é bonito')
print('Tenha um bom dia, {}!'.format(nome))
