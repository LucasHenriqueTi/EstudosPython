"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que Posição está Determinado Time."""

times = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Internacional', 'Athletico-PR', 'Atlético Mineiro',
         'Santos', 'América-MG', 'Bragantino', 'Goiás', 'São Paulo')
print(f'os 5 primeiros colocados são {times[:5]}')
print(f'os 4 ultimos colocados são {times[-4:]}')
print(f'os times em ordem alfabetica são {sorted(times)}')
n1 = str(input('qual time vc quer saber a colocação? ')).title()
print(f'o time {n1} esta na posição {times.index(n1)+1}ª')
