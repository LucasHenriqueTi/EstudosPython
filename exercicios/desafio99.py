"""Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""


def maior(* num):
    print(f'você digitou {len(lista)} números e o maior deles é {max(lista)} ')


lista = []
while True:
    lista.append(int(input('digite um numero: ')))
    if lista[-1] == 999:
        lista.pop()
        break

maior(lista)
