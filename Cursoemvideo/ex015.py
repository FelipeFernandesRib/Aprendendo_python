dias = int(input('Informe por quantos dias o carro ficou alugado: '))
km_rodado = float(input('Informe quantos km foram rodados: '))
print('Valor a ser pago em R$: {}'.format(dias * 60 + km_rodado * 0.15))
