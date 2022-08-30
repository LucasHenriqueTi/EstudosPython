"""lista = [['pedro', 19], ['maria', 22], ['lucas', 24]]
lista.sort()
for p in lista:
    print(p)"""

"""listacopia = []
listaoriginal = []
for c in range(0, 3):
    listaoriginal.append(str(input('nome: ')))
    listaoriginal.append(int(input('idade: ')))
    listacopia.append(listaoriginal[:])
    listaoriginal.clear()
print(listacopia)"""

listacopia = []
listaoriginal = []
homem = mulher = 0
for c in range(0, 3):
    listaoriginal.append(str(input('nome: ')))
    listaoriginal.append(int(input('idade: ')))
    listaoriginal.append(str(input('sexo: ')))
    listacopia.append(listaoriginal[:])
    listaoriginal.clear()
for p in listacopia:
    if p[1] > 18:
        print(f'{p[0]} tem mais de 18 anos')