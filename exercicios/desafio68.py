"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """

from random import randint
vitorias = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('digite um número: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar: [P/I] ')).upper().strip()[0]
    print(f'Você digitou o número {jogador} e o computador {computador}, o total da {total}', end=' ')
    print('PAR' if total % 2 == 0 else 'IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!')
            vitorias += 1
        else:
            print('Você Perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Ganhou!!')
            vitorias += 1
        else:
            print('Você Perdeu!!')
            break
print(f'Você venceu {vitorias} seguidas!')
