from math import ceil
media=0
homem=''
velho=0
for c in range(1,5):
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=str(input('''Quando o seu Gênero. Digite 'H' para Homem ou 'M' para Mulher: ''')).lower()
    if sexo=='h':
        media += idade
        if idade > velho:
            velho = idade
        if idade == velho:
            homem=nome

print('A média de idade do grupo é de {} '.format(ceil(media/3)))
print('O homem mais velho é o {} e ele tem {} anos!'.format(homem,velho))
