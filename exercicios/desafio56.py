from math import ceil
media=0
homem=''
velho=0
mulher=''
for c in range(1,4):
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=str(input('''Quando o seu Gênero. Digite 'H' para Homem ou 'M' para Mulher: ''')).lower()
    if sexo=='h':
        if idade > velho:
            velho = idade
        if idade == velho:
            homem=nome

    #media += idade
#print('A média de idade do grupo é de {} '.format(ceil(media/3)))
print(velho)
print(homem)