'''c = 1
while c < 10:
    print(c)
    c += +1'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('fim')'''

#sabendo quais numeros digitados são pares ou ímpares
n1 = 1
par = impar = 0
while n1 != 0:
    n1 = int(input('digite um número: '))
    if n1 != 0:
        if n1 % 2 == 0:
            par += +1
        else:
            impar += +1
print('você digitou {} numeros pares e {} números ímpares'.format(par, impar))
