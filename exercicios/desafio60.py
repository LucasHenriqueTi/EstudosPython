"""Faça um programa que leia um número qualquer e mostre o seu fatorial."""

from math import factorial
n = int(input('digite um numero: '))
s1 = factorial(n)
print('o fatorial de {} é {}'.format(n,s1))