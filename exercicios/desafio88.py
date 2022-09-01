"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta."""

from random import randint
jogos = int(input('quantos jogos você quer jogar? '))
for i, p in enumerate(range(0, jogos)):
    listap = []
    while True:
        num = randint(1, 60)
        if num not in listap:
            listap.append(num)
        if len(listap) == 6:
            break
    listap.sort()
    print(f'{i+1}º Jogo: {listap}')
    