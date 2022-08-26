""" Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

from random import randint
num = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
for c in num:
    print(c, end=' ')
print(f'\no maior valor foi {max(num)}')
print(f'o menor valor foi {min(num)}')
