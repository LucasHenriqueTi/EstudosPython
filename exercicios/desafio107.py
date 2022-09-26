"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""

from modulo107 import moeda
num = int(input('digite um numero: '))
print(f'o dobro de {num} é {moeda.dobro(num)}')
print(f'o valor {num} com 13% de acrescimo fica {moeda.aumentar(num)}')
print(f'o valor {num} com 13% de desconto fica {moeda.diminuir(num)}')
print(f'a metade de  {num} é {moeda.metade(num)} ')
