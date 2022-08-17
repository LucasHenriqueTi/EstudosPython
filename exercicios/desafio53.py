frase = str(input('digite uma frase: ')).strip().upper()
#para separada a frase
palavras = frase.split()
#para tirar os espaços
junto = ''.join(frase)

inverso = ''
for c in range(len(frase) - 1, -1, -1):
    inverso += junto[c]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('termos um palíndromo')
else:
    print('a frase digitada não é um palíndromo')

#tbm da pra usar fatiamento
#inverso = junto[::-1]

