"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

num = (int(input('digite um numero: ')),
       int(input('digite outro numero: ')),
       int(input('digite mais um numero: ')),
       int(input('digite o ultimo numero: ')))
print(f'{num}')
print(f'o número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'o número 3 aparece na posição {num.index(3)+1}ª')
else:
    print('nenhum número 3 foi digitado ')
print(f'os números pares digitados foram',end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=', ')
