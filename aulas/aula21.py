"""def somar(a=0, b=0, c=0):
    soma = a + b + c
    return soma


r1 = somar(12, 22)
r2 = somar(12, 1)
r3 = somar(12, 45)"""


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input('digite um numero: '))
if par(n):
    print('é par')
else:
    print('é impar')