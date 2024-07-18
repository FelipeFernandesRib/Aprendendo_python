import random

alu1 = str(input('Informe o nome do primeiro aluno: '))
alu2 = str(input('Informe o nome do segundo aluno: '))
alu3 = str(input('Informe o nome do terceiro aluno: '))
alu4 = str(input('Informe o nome do quarto aluno: '))
lista = '{}, {}, {}, {}'.format(alu1, alu2, alu3, alu4) .split()
random.shuffle(lista)
print('\nA sequêcia sorteada foi : {}'.format(lista))
##print('\nA sequêcia sorteada foi : {}'.format(random.sample([alu1, alu2, alu3, alu4, ], k=4)))