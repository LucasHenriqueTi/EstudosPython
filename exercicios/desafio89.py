listap = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    listap.append([nome, [nota1, nota2], (nota1+nota2)/2])
    sair = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
print(listap)
