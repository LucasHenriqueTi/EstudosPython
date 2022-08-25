"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso."""

números = ('Zero', 'Um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    número = int(input('Digite um número entre 0 e 10: '))
    if número < 0 or número > 10:
        while True:
            número = int(input('Tente Novamentem, Digite um número entre 0 e 10: '))
            if 0 <= número <= 10:
                break
    print(números[número])
    stop = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if stop == 'N':
        break
