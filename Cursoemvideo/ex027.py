nome_completo = input('Digite o seu nome completo: ')
nome_dividido = nome_completo.split()
print('Primeiro nome: {}'.format(nome_dividido[0]))
quant_espac = nome_completo.count(' ')
print('Último nome: {}'.format(nome_dividido[quant_espac]))
