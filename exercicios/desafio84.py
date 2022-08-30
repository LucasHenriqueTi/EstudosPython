listaprincipal = []
listasecundaria = []
pesadas = []
leves = []
contador = 0
while True:
    listasecundaria.append(str(input('Nome:')))
    listasecundaria.append(int(input('Peso:')))
    listaprincipal.append(listasecundaria[:])
    listasecundaria.clear()
    contador += 1
    sair = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break

for p in listaprincipal:
    if p[0] > 70:
        pesadas += p[1]
    print(pesadas)
