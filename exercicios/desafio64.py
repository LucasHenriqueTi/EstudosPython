sair = 0
total = 0
soma = 0
print('digite números para saber a soma entre eles, se quiser sair, digite 999.')
while sair != 999:
    numero = int(input('digite números: '))
    if numero == 999:
        sair = 999
    else:
        total += 1
        soma += numero
print('você digitiou {} números e a soba entre eles da {}'.format(total, soma))
