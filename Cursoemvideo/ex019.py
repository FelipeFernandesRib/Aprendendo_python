import random

alu1 = str(input('Informe o nome do primeiro aluno: '))
alu2 = str(input('Informe o nome do segundo aluno: '))
alu3 = str(input('Informe o nome do terceiro aluno: '))
alu4 = str(input('Informe o nome do quarto aluno: '))
print('\nO aluno escolhido foi o: {}'.format(random.choice([alu1, alu2, alu3, alu4])))
