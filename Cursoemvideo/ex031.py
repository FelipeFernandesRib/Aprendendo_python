d = float(input('Informe em km a distância que sua viagem terá: '))
if d > 200:
    print('O valor a pagar seria de R$: {}'.format(d * 0.45))
else:
    print('O valor a pagar seria de R$: {}'.format(d * 0.5))
