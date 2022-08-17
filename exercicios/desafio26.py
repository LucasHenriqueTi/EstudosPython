n1= str(input('digite uma frase: ')).strip().lower()
print('sua frase tem um total de {} letras A'.format(n1.count('a')))
print('a primeira letra a aparece na posição {}'.format(n1.find('a')))
print('a letra A aparece por ultimo na posição {}'.format(n1.rfind('a')))
