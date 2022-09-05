""" Crie um programa que gerencie o aproveitamento de um jogador de futebol.
 O programa vai ler o nome do jogador e quantas partidas ele jogou.
 Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

dados = {'nome': str(input('Nome do jogador: '))}
lista = []
dados['gols'] = lista
dados['total'] = sum(lista)
jogos = int(input(f'quantas partidas {dados["nome"]} jogou? '))
for c in range(0, jogos):
    lista.append(int(input(f'Quantos Gols {dados["nome"]} fez na {c+1}ª partida ? ')))
for k, v in dados.items():
    print(f'o campo {k} tem o valor de {v}')
print('=-' * 30)
print(f'o jogador {dados["nome"]} jogou {jogos}')
for i, v in enumerate(lista):
    print(f'Na {i+1}º partida, fez {v} Gols ')
print(f'foram um total de {sum(lista)}')
