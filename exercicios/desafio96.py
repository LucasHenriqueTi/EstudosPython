"""Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""


def area(a, b):
    print(f'A área de um terreno {a}x{b} é de {a*b}m²')


num1 = float(input('Largura: (m) '))
num2 = float(input('Altura: (m) '))
area(num1, num2)
