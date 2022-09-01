"""Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente."""

listap = [[], []]
for c in range(0, 7):
    num = int(input(f'digite {c+1}º número: '))
    if num % 2 == 0:
        listap[0].append(num)
    else:
        listap[1].append(num)
listap[0].sort()
listap[1].sort()
print(f'os números pares são {listap[0]}')
print(f'os números ímpares são {listap[1]}')
