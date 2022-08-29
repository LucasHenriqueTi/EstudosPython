"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. """

lista = []
for c in range(0, 5):
    lista.append(int(input('digite um número: ')))
print(f'você digitou {lista}')
print(f'o menor valor digitado foi {min(lista)}, na posições', end=' ')
menor = min(lista)
for c, v in enumerate(lista):
    if v == menor:
        print(f'{c}...', end=' ')
print(f'\no maior valor digitado foi {max(lista)}, na posições', end=' ')
maior = max(lista)
for c, v in enumerate(lista):
    if v == maior:
        print(f'{c}...', end=' ')
