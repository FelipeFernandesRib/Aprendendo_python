n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
n3 = int(input('Informe mais um número: '))

print('Analizando os números\n')

if n1 > n2 and n1 > n3:
    print('O número {} é o maior dos 3'.format(n1))

if n2 > n1 and n2 > n3:
    print('O número {} é o maior dos 3'.format(n2))

if n3 > n1 and n3 > n2:
    print('O número {} é o maior dos 3'.format(n3))

if n1 < n2 and n1 < n3:
    print('O número {} é o menor dos 3'.format(n1))

if n2 < n1 and n2 < n3:
    print('O número {} é o menor dos 3'.format(n2))

if n3 < n1 and n3 < n2:
    print('O número {} é o menor dos 3'.format(n3))

if n1 == n2 or n2 == n3:
    print('Você informou números iguais')
