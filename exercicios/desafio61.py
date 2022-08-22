"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while."""

n1 = int(input('digite o primeiro termo: '))
razao = int(input('digite a razão: '))
termo = n1
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += +1
print('FIM')
