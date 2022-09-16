"""Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável."""


def inutil(inu):
    tam = len(inu) + 2
    print('=' * tam)
    print(f' {inu}')
    print('=' * tam)


texto = str(input('digite algo: '))
inutil(texto)
