"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
computador = randint(0, 10)
maismenos = ''
tentativas = -1
acertou = False
print('o computador pensou em um número, você consegue adivinhar? ')
while not acertou:
    jogador = int(input('Qual o seu Palpite: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    if jogador > computador:
        print('Menos..., tente novamente!!')
    elif jogador < computador:
        print('Mais..., tente novamente')
print('Você acertou na tentativa {} !!, o número que o computador pensou foi o {}'.format(tentativas+1, computador))
