"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """

total = cont = menorp = produtos = 0
produto = ' '
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do Produto: R$'))
    produtos += 1
    if preço >= 1000:
        cont += 1
    if produtos == 1 or preço < menorp:
        menorp = preço
        produto = nome
    total += preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O valo total das compras é R${total:.2f}')
print(f'{cont} Produtos Passam de R$1000')
print(f'o produto com menor preço é a(o) {produto} R${menorp:.2f}')
