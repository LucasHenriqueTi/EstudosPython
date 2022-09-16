"""def altentificação(msg):
    print('=-' * 30)
    print(msg)
    print('=-' * 30)

altentificação('LUCAS')"""


"""def soma(n1, n2):
    print(f'{n1 + n2}')


while True:
    num1 = int(input('digite um um valor: '))
    num2 = int(input('digite um um valor: '))
    if num1 and num2 >= 0:
        soma(num1, num2)
        break"""


def dobra(lst):
    posição = 0
    while posição < len(lst):
        lst[posição] *= 2
        posição += 1


lista = []
for c in range(0, 2):
    lista.append(int(input('digite um numero')))
dobra(lista)
print(lista)


