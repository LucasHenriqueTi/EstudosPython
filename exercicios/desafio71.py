""" Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues."""

totalced = 0
dinheiro = 50
valor = int(input('Qual Valor você quer sacar: R$'))
total = valor
while True:
    if total >= dinheiro:
        total -= dinheiro
        totalced += 1
    else:
        print(f'total de {totalced} cédulas de R${dinheiro:.2f}')
        if dinheiro == 50:
            dinheiro = 20
        elif dinheiro == 20:
            dinheiro = 10
        elif dinheiro == 10:
            dinheiro = 1
        totalced = 0
        if total == 0:
            break
