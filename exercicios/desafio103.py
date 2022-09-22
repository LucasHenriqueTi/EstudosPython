""" Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
 O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado """


def ficha(nome='desconhecido', gols=0):
    print(f'o jogador {nome} fez {gols} nesse campeonato.')


nome1 = str(input('nome do jogador: '))
gols1 = str(input('numero de gols: '))
if gols1.isnumeric():
    gols1 = int(gols1)
else:
    gols1 = 0
if nome1.strip() == '':
    ficha(gols=gols1)
else:
    ficha(nome1, gols1)

