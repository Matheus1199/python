nome = input('Escreva seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro é {} e tem {} letras'.format(nome., nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))