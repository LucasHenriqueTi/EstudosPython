#Exercício Python 056: desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
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
media = 0
homem = ''
velho = 0
mulher = 0
for c in range(1, 5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('''Quando o seu Gênero. Digite 'M' para mascúlino ou 'F' para Fêminino: ''')).lower()
    if sexo == 'm':
        if idade > velho:
            velho = idade
        if idade == velho:
            homem = nome
    if sexo == 'f':
        if idade < 20:
            mulher += +1
    media += idade
print('A média de idade do grupo é de {} '.format(ceil(media/4)))
if homem == '':
    print('Não existe homens nessa lista')
else:
    print('O homem mais velho é o {}, ele tem {} anos'.format(homem.title(), velho))
print('Ao todos são {} mulheres com menos de 20 anos!'.format(mulher))

