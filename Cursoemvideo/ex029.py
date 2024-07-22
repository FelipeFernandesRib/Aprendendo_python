vel = float(input('Informe a velocidade do carro: '))
if vel > 80:
    print('Você ultrapassou o limite de velocidade, sua muta será de R$: {:.0f}'.format((vel - 80)*7))
else:
    print('Parabéns por andar dentro do limite de velocidade')
