"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
 a soma entre todos os valores pares sorteados pela função anterior."""

from random import randint

numeros = []


def sort(lista):
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print(numeros)


def soma(num):
    somapar = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            somapar += v
    print(somapar)


sort(numeros)
soma(numeros)
