salario = float(input('Informe o valor do seu salário: '))
if salario > 1250:
    print('Com o aumento salárial de 10%, você passará a ganhar R$:{:.2f}'.format(salario * 1.10))
else:
    print('Com o aumento salárial de 15%, você passará a ganhar R$:{:.2f}'.format(salario * 1.15))
