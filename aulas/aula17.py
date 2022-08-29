"""num = [1, 2, 3, 4, 2]
num.insert(2, 3)
while 2 in num:
    num.remove(2)
    if 2 not in num:
        break
print(num)"""

"""num = []
num.append(8)
num.append(9)
num.append(7)
num.append(3)
num.sort()
for c, v in enumerate(num):
    print(f'na posição {c} encontrei os valores {v}')"""

"""lista = []
for contador in range(0, 5):
    lista.append(int(input('digite um valor')))
for c, v in enumerate(lista):
    print(f'na posição {c} foi digitado o valor de {v}')"""

lista = []
while True:
    lista.append(int(input('digite um número: ')))
    if len(lista) > 5:
        break
for c, v in enumerate(lista):
    print(f'os números digitados foram {v}')
