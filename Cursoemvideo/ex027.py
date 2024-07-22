nome_completo = str(input('Digite o seu nome completo: '))
nome_dividido = nome_completo.split()
print('Primeiro nome: {}'.format(nome_dividido[0]))
print('Último nome: {}'.format(nome_dividido[len(nome_dividido)-1]))
