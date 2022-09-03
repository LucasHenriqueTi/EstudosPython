"""filmes = {'nome': 'star wars',
          'ano': 1997,
          'diretor': 'George lucas'}
for k, v in filmes.items():
    print(f'o {k} é {v}')"""

cadastro = {}
lista = []
for c in range(0, 3):
    cadastro['nomes'] = str(input('Nome: '))
    cadastro['idade'] = int(input('Idade: '))
    lista.append(cadastro.copy())
for c in lista:
    for k, v in c.items():
        print(f'{k} - {v}')
        