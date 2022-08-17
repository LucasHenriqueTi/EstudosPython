soma = 0
for c in range (1,7):
    n1=(int(input('digite {}º número: '.format(c))))
    if n1 % 2 == 0:
        soma += n1
print('a soma entre os números pares é de {}'.format(soma))
