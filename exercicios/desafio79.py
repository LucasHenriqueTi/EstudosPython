"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente. """

lista = []
while True:
    n1 = (int(input('digite um numero: ')))
    num = n1
    if num in lista:
        print('valor repetido')
    else:
        lista.append(num)
        print('numero adicionado!')
    sair = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
lista.sort()
print(lista)
