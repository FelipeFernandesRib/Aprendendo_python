import random
n = random.randint(0, 5)
num = int(input('Digite o número que você acha que o computador sorteou: '))
if num == n:
    print('Parabéns, você venceu')
else:
    print('Infelizmente o computador venceu')
