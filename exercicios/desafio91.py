"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário em Python.No final, coloque esse dicionário em ordem
sabendo que o vencedor tirou o maior número no dado."""

import operator
from random import randint
jogadores = {'p1': randint(0, 6), 'p2': randint(0, 6), 'p3': randint(0, 6), 'p4': randint(0, 6)}
print('Valores Sorteados')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
print('Ranking dos jogadores')
rank = (sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True))
for i, v in enumerate(rank):
    print(f'{i+1}º foi {v[0]} com {v[1]}')
