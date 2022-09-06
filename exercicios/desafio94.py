lista = []
dados = {}
cont = num = 0
while True:
    dados.clear()
    dados = {'nome': str(input('Nome: ')),
             'sexo': str(input('Sexo: ')),
             'idade': int(input('Idade: '))}
    num += dados['idade']
    lista.append(dados.copy())
    cont += 1
    sair = str(input('continuar ? [S/N]')).upper().strip()[0]
    if sair == 'N':
        break
for p in lista:
    if dados['sexo'] == 'f':
        print(f'{dados["nome"]}', end=' ')
