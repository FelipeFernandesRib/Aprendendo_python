r1 = float(input('Informe o valor da reta 1: '))
r2 = float(input('Informe o valor da reta 2: '))
r3 = float(input('Informe o valor da reta 3: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Com os valores apresentados seria possível former um triângulo')
else:
    print('Com esses valores nâo seria possível formar um triângulo')