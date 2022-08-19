"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

#resultado sozinho
n1 = int(input('Digite o 1º Número: '))
n2 = int(input('Digite o 2º Número: '))
sair = False
while not sair:
    menu = int(input('''Selecione uma das opções a baixo:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa 
'''))
    if menu == 1:
        print('O resultado de  {} + {} é: {}'.format(n1, n2, n1+n2))
        print('=*' * 20)
    elif menu == 2:
        print('O resiltado de {} x {} é: {} '.format(n1, n2, n1*n2))
        print('=*' * 20)
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número é {}'.format(maior))
        print('=*' * 20)
    elif menu == 4:
        n1 = int(input('Digite o 1º Número: '))
        n2 = int(input('Digite o 2º Número: '))
        print('=*' * 20)
    elif menu == 5:
        print('finalizando o programa!')
        sair = True
    else:
        print('OPÇÃO INVALIDA')
