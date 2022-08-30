"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""

lista = []
par = []
impar = []
while True:
    numeros = int(input('digite um numero: '))
    lista.append(numeros)
    if numeros % 2 == 0:
        par.append(numeros)
    else:
        impar.append(numeros)
    sair = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
print(lista)
print(par)
print(impar)
