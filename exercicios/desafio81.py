"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

lista = []
contador = 0
while True:
    lista.append(int(input('digite um número: ')))
    contador += 1
    lista.sort(reverse=True)
    sair = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
if lista.count(5) == 1:
    print(f'o número 5 foi digitado na posição {lista.index(5)+1}')
else:
    print('o número 5 não foi digitado')
print(f'vc digitou {contador} números')
print(lista)
