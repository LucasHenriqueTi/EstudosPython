"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

listaprincipal = []
listasecundaria = []
pesadas = leves = 0
while True:
    listasecundaria.append(str(input('Nome:')))
    listasecundaria.append(int(input('Peso:')))
    if len(listaprincipal) == 0:
        pesadas = leves = listasecundaria[1]
    else:
        if listasecundaria[1] > pesadas:
            pesadas = listasecundaria[1]
        if listasecundaria[1] < leves:
            leves = listasecundaria[1]
    listaprincipal.append(listasecundaria[:])
    listasecundaria.clear()
    sair = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
print(f'foram {len(listaprincipal)} de pessoas cadastradas!')
print(f'o maior peso foi de {pesadas}Kg, peso de', end=' ')
for p in listaprincipal:
    if p[1] == pesadas:
        print(f'{p[0]}', end=' ')
print()
print(f'o menor peso foi de {leves}Kg, peso de', end=' ')
for p in listaprincipal:
    if p[1] == leves:
        print(f'{p[0]}', end=' ')


