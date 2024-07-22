frase = input('Digite um frase: ').strip().lower()
print('A sua frase possui {} letras "a"'.format(frase.count('a')))
print('O primeiro "a" aparece na posição {}'.format(frase.find('a') + 1))
print('O último "a" aparece na posição {}'.format(frase.rfind('a') + 1))
