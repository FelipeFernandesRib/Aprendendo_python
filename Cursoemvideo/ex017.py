import math
oposto = float(input('Informe o valor do cateto oposto: '))
adjacente = float(input('Informe o valor do cateto adjcente: '))
print('O comprimento da hipotenusa é {:.2f}'.format(math.hypot(oposto, adjacente)))
