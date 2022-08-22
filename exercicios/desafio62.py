"""Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos."""

n1 = int(input('digite o primeiro termo: '))
razao = int(input('digite a razão: '))
termo = n1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += +1
    print('PAUSA')
    mais = int(input('Quantos termos você quer ver a mais? '))
    print('FIM')
