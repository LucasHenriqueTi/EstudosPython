lista = []
while True:
    lista.append(int(input('digite um número: ')))

    sair = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
    while True:
        sair2 = str(input('opção invalida, tente novamente: ')).upper().strip()[0]
        if sair2 == 'S':
            break
